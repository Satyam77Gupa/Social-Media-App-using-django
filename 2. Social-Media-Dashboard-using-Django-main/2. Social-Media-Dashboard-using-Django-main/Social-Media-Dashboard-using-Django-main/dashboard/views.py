from django.shortcuts import render
from django.conf import settings
from allauth.socialaccount.models import SocialAccount
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
# dashboard/views.py
import tweepy

@login_required
def home_view(request):
    # This will be your main dashboard view
    # You'll fetch and display aggregated data here
    user_social_accounts = request.user.userprofile.get_social_accounts()
    context = {
        'social_accounts': user_social_accounts,
        'username': request.user.username,
        # 'aggregated_posts': get_aggregated_posts(request.user) # Function to aggregate posts
    }
    return render(request, 'dashboard/home.html', context)


def get_twitter_api(user):
    try:
        twitter_account = SocialAccount.objects.get(user=user, provider='twitter')
        # allauth stores tokens in SocialToken model
        access_token = twitter_account.socialtoken_set.get().token
        access_token_secret = twitter_account.socialtoken_set.get().token_secret

        auth = tweepy.OAuthHandler(settings.SOCIALACCOUNT_PROVIDERS['twitter']['APP']['client_id'],
                                   settings.SOCIALACCOUNT_PROVIDERS['twitter']['APP']['secret'])
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    except SocialAccount.DoesNotExist:
        return None # User has not connected Twitter
    except Exception as e:
        # Handle token expiration or other API errors gracefully
        print(f"Error getting Twitter API for user {user.username}: {e}")
        return None

def twitter_posts_view(request):
    user = request.user
    api = get_twitter_api(user)
    posts = []
    if api:
        try:
            # Fetch user's timeline (e.g., last 10 tweets)
            public_tweets = api.home_timeline(count=10)
            for tweet in public_tweets:
                posts.append({
                    'id': tweet.id_str,
                    'text': tweet.text,
                    'user': tweet.user.screen_name,
                    'created_at': tweet.created_at,
                    'likes': tweet.favorite_count,
                    'retweets': tweet.retweet_count,
                    'platform': 'Twitter'
                })
        except tweepy.TweepyException as e:
            # Handle specific Twitter API errors
            print(f"Twitter API error: {e}")
            # You might want to redirect to an error page or show a message
    return render(request, 'dashboard/twitter_feed.html', {'posts': posts})



@login_required
@require_POST
def like_tweet(request):
    tweet_id = request.POST.get('tweet_id')
    api = get_twitter_api(request.user)
    if api and tweet_id:
        try:
            api.create_favorite(id=tweet_id)
            return JsonResponse({'status': 'success', 'message': 'Tweet liked!'})
        except tweepy.TweepyException as e:
            return JsonResponse({'status': 'error', 'message': f'Error liking tweet: {e}'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request or not authorized'}, status=400)
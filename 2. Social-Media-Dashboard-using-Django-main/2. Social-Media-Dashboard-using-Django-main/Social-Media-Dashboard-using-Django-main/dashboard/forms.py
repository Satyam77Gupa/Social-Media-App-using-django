# dashboard/forms.py
from django import forms
from django.shortcuts import render

class PostForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="What's on your mind?")
    post_to_twitter = forms.BooleanField(required=False, label="Post to Twitter")
    post_to_facebook = forms.BooleanField(required=False, label="Post to Facebook")
    # Add other platforms

# dashboard/views.py
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            post_to_twitter = form.cleaned_data['post_to_twitter']
            post_to_facebook = form.cleaned_data['post_to_facebook']

            messages = []
            if post_to_twitter:
                api = get_twitter_api(request.user)
                if api:
                    try:
                        api.update_status(content)
                        messages.append("Posted to Twitter successfully!")
                    except tweepy.TweepyException as e:
                        messages.append(f"Error posting to Twitter: {e}")
                else:
                    messages.append("Twitter account not connected.")

            if post_to_facebook:
                # Similar logic for Facebook using facebook-sdk
                # Requires a Facebook access token with 'publish_pages' or 'publish_actions' permission
                # This is more complex and might require a Page Access Token for actual posting
                messages.append("Facebook posting not fully implemented yet (requires specific permissions).")

            return render(request, 'dashboard/post_status.html', {'messages': messages})
    else:
        form = PostForm()
    return render(request, 'dashboard/create_post.html', {'form': form})
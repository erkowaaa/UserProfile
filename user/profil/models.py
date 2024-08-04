from django.db import models


class UserProfile(models.Model):
    nickname = models.CharField(max_length=16, unique=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nickname


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='following_set',on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='follower_set',on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower} follows {self.following}"


class Post(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_img/')
    video = models.FileField(verbose_name='Видео',upload_to='video_posts/', null=True, blank=True)
    caption = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    hashtag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.user_name}'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    parent = models.ForeignKey('self', related_name='replies', blank=True, null=True, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'
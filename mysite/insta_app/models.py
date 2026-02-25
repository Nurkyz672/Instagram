from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    avatar = models.ImageField(null=True,blank=True)
    user_link = models.URLField(null=True,blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True,blank= True)
    phone_number =PhoneNumberField
    is_official = models.BooleanField(default=False)
    TypeChoices = (
    ('blog','blog'),
    ('photographier','photographier'),
    ('siger','siger'),
    ('artist','artist')
    )
    user_type = models.CharField(max_length=40,choices=TypeChoices)
    date_registered = models.DateField(auto_now_add=True)

    def str(self):
        return f'{self.username}, {self.password}, {self.email}'


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile,related_name='follower',on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile,related_name='following',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower},{self.following}'


class Hashtag(models.Model):
    hashtag_name = models.CharField()

    def __str__(self):
        return self.hashtag_name

class Location(models.Model):
    location_name = models.CharField()

    def __str__(self):
        return self.location_name

class Post(models.Model):
    author = models.ForeignKey(UserProfile,related_name='author',on_delete=models.CASCADE)
    description = models.TextField()
    music = models.URLField(null=True,blank=True)
    hashtag = models.ManyToManyField(Hashtag, blank=True)
    user = models.ManyToManyField(UserProfile,related_name='users')
    location = models.ForeignKey(Location,null=True,blank=True,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def str(self):
        return f'{self.author},{self.user}'


class PostContent(models.Model):
    post = models.ForeignKey(Post,related_name='content',on_delete=models.CASCADE)
    file = models.FileField(null=True,blank=True)

    def str(self):
        return f'{self.post},{self.file}'


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile,related_name='like',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='likies',on_delete=models.CASCADE)
    like = models.BooleanField()


    


class Comment(models.Model):
    user = models.ForeignKey(UserProfile,related_name='comment',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self',null=True, blank=True,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def str(self):
        return f'{self.post},{self.parent}'


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile,related_name='comment_like',on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,related_name='comment_likes',on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user','comment',)


class Favorite(models.Model):
    user = models.OneToOneField(UserProfile,related_name='favorite',on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite,related_name='favorite',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='favorites',on_delete=models.CASCADE)





class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)



class Message(models.Model):
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)
    video = models.FileField(upload_to='videos',null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)
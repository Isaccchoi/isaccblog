from django.dispatch import receiver
from django.db.models.signals import post_delete
from post.models import Post
from post.models import Comment


@receiver(post_delete, sender=Post)
def delete_attachmented_image(sender, instance, **kwargs):
    if not instance.image:
        return

    instance.image.delete(save=False)

@receiver(post_delete, sender=Post)
def delete_attachmented_comment(sender, instance, **kwargs):
    if not instance.comment_set:
        return

    for comment in Comment.objects.filter(post=instance):
        comment.delete()

        

from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from core.utils.model_utils import TimestampMixin, BaseModel


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<username>/<filename>
    return '{0}/cover/{1}'.format(instance.username, filename)


def user_directory_photo_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<username>/<filename>
    return '{0}/profile/{1}'.format(instance.username, filename)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    cover_image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    profile_image = models.ImageField(upload_to=user_directory_photo_path, blank=True, null=True)


class UserMeta(BaseModel, TimestampMixin):
    user = models.ForeignKey("accounts.User", related_name='user_metas', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self):
        return self.user


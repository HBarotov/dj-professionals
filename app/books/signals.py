from django_cleanup.signals import cleanup_pre_delete
from easy_thumbnails.files import get_thumbnailer


def easy_delete(**kwargs):
    print("Start")
    file = get_thumbnailer(kwargs["file"])
    file.delete_thumbnails()
    print("End")


cleanup_pre_delete.connect(easy_delete)

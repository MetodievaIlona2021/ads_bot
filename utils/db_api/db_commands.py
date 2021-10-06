from asgiref.sync import sync_to_async
from loader import ds
ds()
from django_project.users_manage.models import User, Articles


@sync_to_async
def select_user(user_id: int):
    return User.objects.filter(user_id=user_id).first()


@sync_to_async
def add_user(user_id, full_name, username):
    try:
        return User(user_id=int(user_id), name=full_name, username=username).save()
    except Exception:
        return select_user(int(user_id))


@sync_to_async
def select_all_users():
    return User.objects.all()


@sync_to_async
def count_users():
    return User.objects.all().count()


@sync_to_async
def new_article(**kwargs):
    return Articles(**kwargs).save()


@sync_to_async
def select_all_articles():
    return Articles.objects.all()


@sync_to_async
def select_sorted_articles(search_query: str = None):
    if search_query:
        search_articles = Articles.objects.order_by('id').all()
        # search_articles = Articles.objects.filter('name'.__icontains(f'%{search_query}%')).all()
    else:
        search_articles = Articles.objects.order_by('id').all()

    return search_articles

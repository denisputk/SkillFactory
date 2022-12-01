# 1. Создать двух пользователей (с помощью метода User.objects.create_user('username')):

User.objects.create_user(username = 'Робби', password = 'qwerty', first_name = 'Роберт', last_name = 'Локамп', email = 'robert.lokamp@gmail.com')
User.objects.create_user(username = 'Пат', password = '1234', first_name = 'Патриция', last_name = 'Хольман', email = 'pat@gmail.com')

# 2. Создать два объекта модели Author, связанные с пользователями.
Author.objects.create(user = User.objects.get(username = 'Робби'))
Author.objects.create(user = User.objects.get(username = 'Пат'))

# 3. Добавить 4 категории в модель Category.
Category.objects.create(category_name = 'Развлечения')
Category.objects.create(category_name = 'Финансы')
Category.objects.create(category_name = 'Спорт')
Category.objects.create(category_name = 'Образование')

# 4. Добавить 2 статьи и 1 новость.
Post.objects.create(author = Author(pk=1), post_type = 'AR', title = 'В Эстонии исчезла возможность работать на Twitter', post_content = 'Рождество будет мрачным для десятков сотрудников Sutherland Global Services OÜ: компания сократит почти 80 человек в Таллинне, а рабочие места переведут в Азию. В октябре эстонский филиал Sutherland Global объявил о коллективном сокращении 78 сотрудников. Работники подтвердили порталу Geenius, а позже и Postimees, что работали на Twitter и модерировали посты в социальной среде')
Post.objects.create(author = Author(pk=2), post_type = 'NW', title = 'ЧМ-2022: сборная Австралии обыграла Данию и вышла в плей-офф', post_content = 'На проходящем в Катаре чемпионата мира по футболу в матче группы D сборная Австралии обыграла Данию со счетом 1:0 и вышла в плей-офф. Единственный гол на 60-й минуте забил Мэтью Леки.')
Post.objects.create(author = Author(pk=2), post_type = 'AR', title = 'Avatar 2, (The Way of Water)', post_content = 'The sequel to James Cameron record-breaking movie will take audiences back to Pandora and is sure to be another visually stunning watch, as teased in both the first teaser and the main trailer. Cameron plan has been for the sequel to kickstart a run of movies every other year until Avatar 5 in December 2028. However, he revealed that if The Way of Water underperforms, there is a plan to end it with Avatar 3.')

# 5. Присвоить им категории.
PostCategory.objects.create(post = Post.objects.get(pk=1), category = Category.objects.get(category_name = 'Финансы'))
PostCategory.objects.create(post = Post.objects.get(pk=2), category = Category.objects.get(category_name = 'Спорт'))
PostCategory.objects.create(post = Post.objects.get(pk=2), category = Category.objects.get(category_name = 'Развлечения'))
PostCategory.objects.create(post = Post.objects.get(pk=3), category = Category.objects.get(category_name = 'Развлечения'))

# 6. Создать как минимум 4 комментария к разным объектам модели Post.
Comment.objects.create(post = Post.objects.get(pk=1), user = User.objects.get(username = 'Робби'), comm_content = 'Очень жалко, когда люди теряют работу.')
Comment.objects.create(post = Post.objects.get(pk=2), user = User.objects.get(username = 'Робби'), comm_content = 'Самые великие футбольные державы играли!')
Comment.objects.create(post = Post.objects.get(pk=2), user = User.objects.get(username = 'Пат'), comm_content = 'Как можно этим интересоваться?')
Comment.objects.create(post = Post.objects.get(pk=3), user = User.objects.get(username = 'Пат'), comm_content = 'Очень жду этот фильм!')

# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Post.objects.get(pk=1).dislike()
Post.objects.get(pk=1).dislike()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=3).dislike()
Comment.objects.get(pk=4).like()

# 8. Обновить рейтинги пользователей.
Author.objects.get(pk=1).update_rating()
Author.objects.get(pk=2).update_rating()

# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
Author.objects.all().order_by('-author_rating').values('user__username', 'author_rating')[0]

# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
Post.objects.all().order_by('-post_rating').values('post_created', 'author__user__username', 'post_rating', 'title')[0]
best_post = Post.objects.all().order_by('-post_rating')[0]
best_post.preview()

# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
Comment.objects.filter(post = best_post).values('comm_created', 'user', 'comm_rating', 'comm_content')
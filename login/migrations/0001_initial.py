# Generated by Django 2.2.7 on 2020-05-07 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('profile', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=128)),
                ('link', models.CharField(default='', max_length=256)),
                ('piclink', models.CharField(default='', max_length=256)),
                ('authorlink', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Baidu_Hotnews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='cate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_id', models.CharField(max_length=64, unique=True, verbose_name='ID')),
                ('cate_name', models.CharField(max_length=64, verbose_name='名字')),
            ],
            options={
                'verbose_name_plural': '新闻类别表',
                'db_table': 'cate',
            },
        ),
        migrations.CreateModel(
            name='CSDN_Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('profile', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=128)),
                ('link', models.CharField(default='', max_length=256)),
                ('piclink', models.CharField(default='', max_length=256)),
                ('authorlink', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Hotnews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Jianshu_Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('profile', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=128)),
                ('link', models.CharField(default='', max_length=256)),
                ('piclink', models.CharField(default='', max_length=256)),
                ('authorlink', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Lunbo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunbo_url', models.CharField(default='', max_length=256)),
                ('img', models.CharField(default='', max_length=256)),
                ('lunbo_title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='newbrowse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64, verbose_name='用户名')),
                ('new_id', models.CharField(max_length=64, verbose_name='ID')),
                ('new_browse_time', models.DateTimeField(verbose_name='浏览时间')),
            ],
            options={
                'verbose_name_plural': '用户点击表',
                'db_table': 'newbrowse',
            },
        ),
        migrations.CreateModel(
            name='newsim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_id_base', models.CharField(max_length=64, verbose_name='ID_base')),
                ('new_id_sim', models.CharField(max_length=64, verbose_name='ID_sim')),
                ('new_correlation', models.FloatField(verbose_name='新闻相关度')),
            ],
            options={
                'verbose_name_plural': '新闻相似度表',
                'db_table': 'newsim',
            },
        ),
        migrations.CreateModel(
            name='newtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_tag', models.CharField(max_length=64, verbose_name='标签')),
                ('new_id', models.CharField(max_length=64, verbose_name='ID')),
                ('new_hot', models.FloatField(verbose_name='热度值')),
            ],
            options={
                'verbose_name_plural': '新闻标签表',
                'db_table': 'newtag',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=128, unique=True)),
                ('channel', models.CharField(default=None, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Sina_Hotnews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Sogo_Hotnews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女'), ('none', '保密')], default='保密', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('prefer', models.CharField(default=None, max_length=256)),
                ('channel', models.CharField(default=None, max_length=256)),
                ('user_img', models.CharField(blank=True, default='/static/login/image/user.png', max_length=64, verbose_name='用户头像图片')),
                ('nickname', models.CharField(blank=True, max_length=256)),
                ('truename', models.CharField(blank=True, max_length=256)),
                ('age', models.CharField(blank=True, max_length=256)),
                ('company', models.CharField(blank=True, max_length=256)),
                ('brief', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('last_log_time', models.DateField(verbose_name='最近登录时间')),
                ('active', models.IntegerField(verbose_name='活跃')),
                ('read', models.IntegerField(verbose_name='阅读')),
            ],
        ),
        migrations.CreateModel(
            name='Weixin_Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('profile', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=128)),
                ('link', models.CharField(default='', max_length=256)),
                ('piclink', models.CharField(default='', max_length=256)),
                ('authorlink', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Word_cloud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64, verbose_name='用户名')),
                ('cloud_time', models.DateField(verbose_name='词云记录时间')),
                ('cloud_img', models.CharField(max_length=64, verbose_name='词云图片')),
                ('cloud_dict', models.CharField(blank=True, max_length=256, verbose_name='词云字典')),
            ],
        ),
        migrations.CreateModel(
            name='newhot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_id', models.CharField(max_length=64, unique=True, verbose_name='ID')),
                ('new_hot', models.FloatField(verbose_name='热度值')),
                ('new_cate', models.ForeignKey(on_delete=False, related_name='类别名', to='login.cate')),
            ],
            options={
                'verbose_name_plural': '新闻热度表',
                'db_table': 'newhot',
            },
        ),
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_id', models.CharField(max_length=64, unique=True, verbose_name='ID')),
                ('new_time', models.DateTimeField(blank=True, verbose_name='发表时间')),
                ('comment', models.IntegerField(default='', verbose_name='评论次数')),
                ('likes', models.IntegerField(default='', verbose_name='喜欢次数')),
                ('new_title', models.CharField(max_length=100, verbose_name='标题')),
                ('new_content', models.TextField(verbose_name='新闻内容')),
                ('author', models.CharField(default='', max_length=100, verbose_name='作者')),
                ('authorlink', models.CharField(default='', max_length=256)),
                ('url', models.CharField(default='', max_length=256)),
                ('piclink', models.CharField(default='', max_length=256)),
                ('new_cate', models.ForeignKey(on_delete=False, related_name='类别', to='login.cate')),
            ],
            options={
                'verbose_name_plural': '新闻信息表',
                'db_table': 'new',
            },
        ),
    ]

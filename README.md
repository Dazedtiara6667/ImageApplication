# ImageApplication #
## My First Web Development Project! ##
This was my first ever project and I know it's not perfect but I am happy that I could come this far with just Google!
My biggest help was Google and most importantly StackOverflow.
Everytime I was getting an error say 'table doesn't exist or maybe url doesn't exist' I used to search on Google for hours and when I finally got the error corrected.It would feel like a milestone in my life.
(Like I defeated Thanos..)

### About The App ###
This is a really basic app that I have created(that's all I could manage).You can upload your images by creating albums and can see other user's albums right now,adding and deleting uploaded images is only possible from admin site,trying to work on it.What I can say is that now I will appreciate even a simple application cause now I know they require a lot of effort to make one.

### What did I learn here ###
This was really a good experience,successful or not one should always try to enjoy the journey while they do something.And I had one hell of a time doing this.Doing something like this on a daily basis would be really exciting for me.It was really exciting to do all this stuff and to spend hours on making right that thing that is important.When I saw this project I was like how the hell will I do this but then the same thought had occured when I was trying to do the 14 tasks and then i did do them though I knew nothing.So what I really learnt here is that you should not give up and also google is your best friend..

### How does the app work? ###
So the first the user has to register/login after which finally he can click on upload albums page to upload albums and go to gallery page to view it.In the Upload Albums the user has to fill out the form and then he click on gallery page.If there is no image the page is blank.

### What else can I add? ###

Currently I don't know much but will try to add some more features so that it becomes more user-friendly.

### My approach to the project ###


In my first week I tried to understand what the project wants me to do.My first step was to create a login register page.I was trying to do create the thing in php and mySQL but my mentor said it's better to use django.That's when I learnt about django.So I tried to use it.At first everything went over my head as I was understanding nothing but after trying out things I learnt how we need to create a form for login register using django.I used django forms which was super helpful.Here first i went into forms.py file and created the form class before that I created a model that I would use in forms.py then I had to do some more things like add MEDIA_ROOT,MEDIA_URL add my app in installed apps so that it was actually working.then after that I went into views.py to save the form and there I learnt about the difference between return render and return request and some more things like this.Finally my login page was working up and fine.
Next I started with the albums which took most of my time at first I tried to upload just one image(even that was hell for me) but finally I succeded and it helped me to understand django more clearly.
Then I worked on Comments Section which I did easily as I was able understand how to use django more clearly.All my images were getting stored into a images file under media file.For all these processes I had  html files which I was using under templates section.For login I had one page and for register one page and so on.I use bootstrap to decorate somewhat(only navbar and navbar-brand,that's the only thing I know in BootStrap lol).I was using curly braces to use the django files and form._as_p to use the forms.Now coming to the final part.For albums I had searched hell of a lot and then one day god answered my prayers and I saw a ray of light.I used some things as ZipField to upload albums.Now these statements might be melodramatic but that's how I felt like.So finally I did the last part and I am writing this documentation now which you are reading and wondering what a fool I am.

### Sources ###
#### 1.YouTube ####
#### 2. StackOverflow ####
#### 3. Last but not the least, Google. ####


### Site Address ###
My site is published at http://127.0.0.1:8000/
(which won't work since it's localhost'.will update one with my ip address and port no)


### Site Images ###
![Screenshot from 2020-03-04 22-41-38](https://user-images.githubusercontent.com/53506835/75945538-8701df00-5ec0-11ea-8d90-99a7899be121.png)


![Screenshot from 2020-03-04 22-42-25](https://user-images.githubusercontent.com/53506835/75945637-d3e5b580-5ec0-11ea-90cf-42dda8d5601b.png)

![Screenshot from 2020-03-04 22-42-48](https://user-images.githubusercontent.com/53506835/75945836-66865480-5ec1-11ea-824e-663f68bd522b.png)


![Screenshot from 2020-03-06 11-46-01](https://user-images.githubusercontent.com/53506835/76057673-306bd200-5fa0-11ea-97cb-ea26fd121aaa.png)



![Screenshot from 2020-03-04 22-45-16](https://user-images.githubusercontent.com/53506835/75945987-d1d02680-5ec1-11ea-8d1a-cd78a3e1ccaa.png)



![Screenshot from 2020-03-06 11-43-48](https://user-images.githubusercontent.com/53506835/76057526-cf43fe80-5f9f-11ea-87c9-6b653990e765.png)



![Screenshot from 2020-03-06 11-39-01](https://user-images.githubusercontent.com/53506835/76057337-4331d700-5f9f-11ea-9211-28c34bb77f58.png)


### Coming Up ###
#### To display the comments of users.(Added this feature)
#### Sharing is not yet supported though I am getting unique urls for each image.(Added Links to each Albums)
#### Have to add one help page where I will manually write the queries for some common questions.(Not worked on this part)
#### Allow users to login through Google,Facebook Accounts(Have not worked out on this part.) 

### Improvements and Suggestions ###
I know this is not some next level amazing,fierce application.So please let me know if there are some improvements or any suggestions that I can use.It will be really helpful for me.

### Languages Used ###
#### 1.Django #####
#### 2.HTML ####
#### 3.postgresql(for database) ####
#### 4.Used some BootStrap for styling. ####


### Install Django ###
#### if you don't have pip then; ###
use 'sudo apt install python-pip' or 'sudo apt install python3-pip'
and then use pip install django.

### For starting the project ###
'django-admin startproject projectname'

### For starting the app ###
'python manage.py startapp appname'

### For making Migrations ###
'python manage.py makemigrations', 
'python manage.py migrate'
(sometimes it will show error if datetime is used try to remove all the migrations not the __init__.py file though and run the command once).

### For running server ###
'python manage.py runserver'(Localhost),
'python manage.py ipaddress:port(8000)'
### If any errors you know where to go... ###



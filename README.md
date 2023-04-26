# cinemaapp


#1 at first create venv

  pip install virtualenv
  virtualenv <env-name>

#2 install requirements
  pip install -r requirements.txt

#3 run Celery worker
  celery -A cinemaapp worker -l info
  
#4 run celery beat
  celery -A cinemaapp worker -l info
  
# run django project 
  python manage.py runserver
  
  you can run project using gunicorn also 
  gunicorn --bind 0.0.0.0:8000 cinemaapp:application
  
  ![Screenshot (118)](https://user-images.githubusercontent.com/95032384/234473568-fef4d466-966c-4e93-96a9-d5261c018a2d.png)
![Screenshot (117)](https://user-images.githubusercontent.com/95032384/234473574-b542c01e-2edb-4198-9114-8abae12748ef.png)

## Backend

-   Django
-   Python
-   sqlite

![dj](https://user-images.githubusercontent.com/41604678/107917985-3342b580-6fac-11eb-8364-c297b10d98e5.png)

## Prerequisites

Ubuntu Environment:

1. Install Django
    ```
    $ pip install Django
    ```
2. Install modules in Django
   (cors, rest_framework, allauth)
    ```
    $ pip install django-cors-headers djangorestframework django-allauth
    ```
3. Install extra modules
    ```
    $ pip install finance-datareader bs4
    ```

## How to execute the file

MacOS Environment :apple:

1. Before executing the file you need Python >= 3.1.3 .

2. Open your terminal and go to the directory of the AutoTA file on your terminal.

    ```
    $ cd Backend/autoTA
    ```

3. Start server
    ```
    $ python manage.py runserver
    ```

Then you'll see this on your terminal.

<img width="521" alt="스크린샷 2021-02-15 오후 4 34 54" src="https://user-images.githubusercontent.com/41604678/107917790-d8a95980-6fab-11eb-828b-2c363e035db4.png">

4. As what the terminal said, you can debug the server at http://127.0.0.1:8000/ local server.
   Now You can run the server ! If you want to open the specific api then jump into these urls.

-   back/stocks/ [name='index']
-   back/stocks/ search/<str:keyword>
-   back/stocks/ search/<str:stock_code>
-   back/stocks/ graph/
-   back/news/

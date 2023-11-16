from django.db import models
import requests

class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    # @classmethod 라는 데코레이터를 사용함
    # 호출시 첫번째 인자로 cls를 사용하고 
    # cls는 클래스 자체를 의미하며 바로 Book을 뜻함

    @classmethod
    def insert_data(cls):
        API_KEY = '직접 발급 받아서 쓰세용!!!'
        params = {
            'ttbkey': API_KEY,
            'QueryType': 'ItemNewAll',
            'MaxResults': 10,
            'start': 1,
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101',
        }
        response = requests.get('http://www.aladin.co.kr/ttb/api/ItemList.aspx', params=params)
        data = response.json()
        # 데이터를 모델 인스턴스로 변환하여 저장합니당~
        for item in data['item']:
            params = {
                'isbn': item['isbn'],
                'author': item['author'],
                'title': item['title'],
                'category_name': item['categoryName'],
                'category_id': item['categoryId'],
                'price': item['priceStandard'],
                'fixed_price': item['fixedPrice'],
                'pub_date': item['pubDate'],
            }
            my_model = cls(**params)
            # **parems => 딕셔너리를 매개변수로 받을때 ** 사용

            my_model.save()


# 저랑 파이썬 3일차에 packing unpacking 공부할떄 나왔던 내용인데
# 잘 기억이안나실까봐 적어 놓아요 !!

# 그냥 가변인자 말고도 [키워드 가변인자] 라는 것도 있는데
# 키워드 가변인자는 인자값이 key value의 형태일때  ( 가변인자는 값이 튜플일때 사용했었음 *args)

# 딕셔너리 형태로 parameter에 저장함
# 이때는 별2개


def print_info(**args):
    print(args)

print_info(kevin=1,john=2,bob=3)

# 인자값을 넣을때 딕셔너리 언패킹도 사용 가능하다

di={'kevin':1,'john':2,'bob':3}

def print_info2(**args):
    for i,j in args.items():
        print(i,j)

print_info2(**di)

class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.name = 'ashkan'

    def __call__(self, request):
        print(f'ghabl az view salam {self.name}')

        response = self.get_response(request)

        print(response.msg)
        print(f'bad az view salam {self.name}')

        return response

    def process_view(self, request, mammad, *args, **kwargs):

        print('dakhele process view')

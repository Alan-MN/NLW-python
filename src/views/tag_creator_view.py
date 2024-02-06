from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsable for http interactions
    '''
    def validate_and_crate(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body['product_code']

        print(product_code)
        ## logica de regra de negocio pra criar tags

        #retorno http
        return HttpResponse(status_code=200,body={'hello':'world'})

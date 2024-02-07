from rest_framework.decorators import api_view
from rest_framework.response import Response

from .lexer import Lexer
from .parser import Parser

# Create your views here.
@api_view(["POST"])
def get_table(request):
    print("REQUEST DATA ", request.data["code"])
    content = request.data["code"]
    lexer = Lexer(content)
    content_output = lexer.to_token()

    parser = Parser(content_output)
    errors = parser.parse()


    if errors == []:
        new_lexemes = [str(i) for i in content_output]
        lexeme = [i[i.find(" "):].strip() for i in new_lexemes]
        token = [i[:i.find(" ")].strip() for i in new_lexemes]
        return Response({"code": str(content),
                        "error": False,
                        "lexeme": list(lexeme),
                        "token": list(token)})
    else:
        errors_list = [str(i) for i in errors]
        errors_value = [i.lexeme for i in errors]
        print(errors_list)
        return Response({
                        "error": True,
                        "errors": list(errors_list),
                        "lexemes": list(errors_value)})

    return Response("hello")
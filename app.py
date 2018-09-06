from apistar import App,Route, http, exceptions


def welcome(name=None):
    if name is None:
        return{'message':'Welcome to API Star!'}
    return{'message':'Welcome to API Star,%s!%name'}

def echo_request_info(request: http.Request) -> dict:
    return{
            'method':request.method,
            'url' : request.url,
            'headers':dict(request.headers),
            'body' : request.body.decode('utf-8')
            }
def echo_query_params(query_params:http.QueryParams)->dict:
    return{
            'params':dict(query_params)
            }
def echo_user_agent(user_agent:http.Header) -> dict:
    return{
        'user-agent':user_agent
        }
def hello_world(accept_language:http.Header)-> http.JSONResponse:
    if 'de' in accept_language:
        data={'text':'Hallo, Welt!'}
    else:
        data = {'text':'Hello, world!'}
        headers = {'Vary': 'Accept-Language'}
        return http.JSONResponse(data, status_code=200, headers=headers)
def hello_wrold() -> http.Response:
    content = 'Hello, world!'
    headers = {'Content-Type':'text/plain'}
    return http.Response(content,headers=headers)
def echo_username(username:str) -> dict:
    return {'message':'Welcome, %s!'%username}



routes=[
        Route("/",method='GET',handler=welcome),
        Route("/users/{username}/",method='GET',handler=echo_username),
        Route("/hello_world",method='GET',handler=hello_world),
        Route("/hellowrold",method='GET',handler=hello_wrold),
        Route("/echo_request_info",method='GET',handler=echo_request_info),
        Route("/echo_query_params",method='GET',handler=echo_query_params),
        Route("/echo_user_agent",method='GET',handler=echo_user_agent),
        ]
app = App(routes=routes)

if __name__=='__main__':
    app.serve('127.0.0.1',5000,debug=True)

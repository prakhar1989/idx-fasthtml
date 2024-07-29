from fasthtml.common import *
import argparse

# Learn more about FastHTML https://docs.fastht.ml/

app,rt = fast_app()

@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")

@rt('/change')
def get(): return P('Nice to be here!')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, help='Port to run the server on', required=True)
    args = parser.parse_args()
    serve(port=args.port)
 
if __name__ == "__main__":
    main()
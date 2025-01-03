from flask import Blueprint, abort
from flask import current_app as app
from flask import make_response, send_from_directory

index = Blueprint("index", __name__)


@index.route("/termos_uso", methods=["GET"])
def termos_uso():
    """
    Rota para servir o arquivo "Termos de Uso.pdf".

    Esta rota responde a requisições GET e retorna o arquivo PDF "Termos de Uso.pdf"
    localizado no diretório configurado em `app.config["PDF_PATH"]`.

    Returns:
        Response: Um objeto de resposta contendo o arquivo PDF e o cabeçalho de tipo MIME
        definido como "application/pdf".

    Raises:
        HTTPException: Retorna um erro 500 se ocorrer qualquer exceção durante o processo.
    """
    try:
        filename = "Termos de Uso.pdf"
        url = send_from_directory(app.config["PDF_PATH"], filename)
        # Crie a resposta usando make_response
        response = make_response(url)

        # Defina o tipo MIME como application/pdf
        response.headers["Content-Type"] = "application/pdf"
        return url

    except Exception as e:
        abort(500, description=str(e))


@index.route("/politica_privacidade", methods=["GET"])
def politica_privacidade():
    """
    Rota para servir o arquivo de Política de Privacidade em formato PDF.

    Tenta enviar o arquivo "Política de Privacidade.pdf" do diretório configurado em "PDF_PATH".
    Define o tipo MIME da resposta como "application/pdf".

    Returns:
        Response: A resposta contendo o arquivo PDF.

    Raises:
        HTTPException: Se ocorrer algum erro ao tentar enviar o arquivo, retorna um erro 500 com a descrição do erro.
    """
    try:
        filename = "Política de Privacidade.pdf"
        url = send_from_directory(app.config["PDF_PATH"], filename)
        # Crie a resposta usando make_response
        response = make_response(url)

        # Defina o tipo MIME como application/pdf
        response.headers["Content-Type"] = "application/pdf"
        return url

    except Exception as e:
        abort(500, description=str(e))

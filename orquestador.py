from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from my_keys import GEMINI_API_KEY
from my_models import GEMINI_PRIMARY

from herramienta_consulta_op import HerramientaConsultaOP
from herramienta_ultima_op_cliente import HerramientaUltimaOPCliente
from herramienta_trabajos_similares import HerramientaTrabajosSimilares
from herramienta_analisis_pdf import HerramientaAnalisisPDF


class AgenteOrquestador:


    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            api_key=GEMINI_API_KEY,
            model=GEMINI_PRIMARY,
            temperature=0
        )


        self.tools = [
            HerramientaConsultaOP(),
            HerramientaUltimaOPCliente(),
            HerramientaTrabajosSimilares(),
            HerramientaAnalisisPDF()
        ]


        self.prompt = hub.pull(
            "hwchase17/react"
        )


        self.agent = create_react_agent(
            self.llm,
            self.tools,
            self.prompt
        )


        self.executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True
        )


    def ejecutar(self, pregunta):

        respuesta = self.executor.invoke(
            {
                "input": pregunta
            }
        )

        return respuesta
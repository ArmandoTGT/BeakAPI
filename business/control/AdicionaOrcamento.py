import sys
import uuid

linux_origin_path = "/.."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from business.model.Orcamento import Orcamento
from infra.RamOrcamentoDAO import RamOrcamentoDAO


def AdicionaOrcamento(nome, profissional, orcamento, id_servico):
    DAO = RamOrcamentoDAO()

    generate_id = str(uuid.uuid4()).split('-')
    id = str(id_servico) + generate_id[0] + generate_id[1]
   
    orcamento = Orcamento(id, nome, profissional, orcamento, id_servico)

    DAO.insere_orcamento(orcamento)

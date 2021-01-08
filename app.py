# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from enum import Enum
from typing import Optional, Any, List, TypeVar, Type, Callable, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class Cor(Enum):
    FF0000 = "#ff0000"
    THE_0000_FF = "#0000ff"
    THE_008000 = "#008000"
    THE_00_FFFF = "#00ffff"

class Artilheiros:
    time:str
    gols:int
    nome_jogador:str

    def __init__(self,time,gols,nome_jogador):
        self.time = time
        self.gols = gols
        self.nome_jogador = nome_jogador

    @staticmethod
    def from_dict(obj: Any) -> 'Artilheiros':
        assert isinstance(obj, dict)
        time = from_str(obj['time'])
        gols = from_int(obj['gols'])
        nome_jogador = from_str(obj['nome'])
        return Artilheiros(time,gols,nome_jogador)

    def to_dict(self) -> dict:
        result:dict = {}
        result["time"] = self.time;
        result["gols"] = self.gols;
        result["nome_jogador"] = self.nome_jogador
        return result

class FaixaClassificacao:
    cor: Optional[Cor]

    def __init__(self, cor: Optional[Cor]) -> None:
        self.cor = cor

    @staticmethod
    def from_dict(obj: Any) -> 'FaixaClassificacao':
        assert isinstance(obj, dict)
        cor = from_union([from_none, Cor], obj["cor"])
        return FaixaClassificacao(cor)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cor"] = from_union([from_none, lambda x: to_enum(Cor, x)], self.cor)
        return result


class UltimosJogo(Enum):
    D = "d"
    E = "e"
    V = "v"


class Classificacao:
    aproveitamento: float
    derrotas: int
    empates: int
    equipe_id: int
    escudo: str
    faixa_classificacao: FaixaClassificacao
    faixa_classificacao_cor: Optional[Cor]
    gols_contra: int
    gols_pro: int
    jogos: int
    nome_popular: str
    ordem: int
    pontos: int
    saldo_gols: int
    sigla: str
    ultimos_jogos: List[UltimosJogo]
    variacao: int
    vitorias: int

    def __init__(self, aproveitamento: float, derrotas: int, empates: int, equipe_id: int, escudo: str, faixa_classificacao: FaixaClassificacao, faixa_classificacao_cor: Optional[Cor], gols_contra: int, gols_pro: int, jogos: int, nome_popular: str, ordem: int, pontos: int, saldo_gols: int, sigla: str, ultimos_jogos: List[UltimosJogo], variacao: int, vitorias: int) -> None:
        self.aproveitamento = aproveitamento
        self.derrotas = derrotas
        self.empates = empates
        self.equipe_id = equipe_id
        self.escudo = escudo
        self.faixa_classificacao = faixa_classificacao
        self.faixa_classificacao_cor = faixa_classificacao_cor
        self.gols_contra = gols_contra
        self.gols_pro = gols_pro
        self.jogos = jogos
        self.nome_popular = nome_popular
        self.ordem = ordem
        self.pontos = pontos
        self.saldo_gols = saldo_gols
        self.sigla = sigla
        self.ultimos_jogos = ultimos_jogos
        self.variacao = variacao
        self.vitorias = vitorias

    @staticmethod
    def from_dict(obj: Any) -> 'Classificacao':
        assert isinstance(obj, dict)
        aproveitamento = from_float(obj["aproveitamento"])
        derrotas = from_int(obj["derrotas"])
        empates = from_int(obj["empates"])
        equipe_id = from_int(obj["equipe_id"])
        escudo = from_str(obj["escudo"])
        faixa_classificacao = FaixaClassificacao.from_dict(obj["faixa_classificacao"])
        faixa_classificacao_cor = from_union([from_none, Cor], obj["faixa_classificacao_cor"])
        gols_contra = from_int(obj["gols_contra"])
        gols_pro = from_int(obj["gols_pro"])
        jogos = from_int(obj["jogos"])
        nome_popular = from_str(obj["nome_popular"])
        ordem = from_int(obj["ordem"])
        pontos = from_int(obj["pontos"])
        saldo_gols = from_int(obj["saldo_gols"])
        sigla = from_str(obj["sigla"])
        ultimos_jogos = from_list(UltimosJogo, obj["ultimos_jogos"])
        variacao = from_int(obj["variacao"])
        vitorias = from_int(obj["vitorias"])
        return Classificacao(aproveitamento, derrotas, empates, equipe_id, escudo, faixa_classificacao, faixa_classificacao_cor, gols_contra, gols_pro, jogos, nome_popular, ordem, pontos, saldo_gols, sigla, ultimos_jogos, variacao, vitorias)

    def to_dict(self) -> dict:
        result: dict = {}
        result["aproveitamento"] = to_float(self.aproveitamento)
        result["derrotas"] = from_int(self.derrotas)
        result["empates"] = from_int(self.empates)
        result["equipe_id"] = from_int(self.equipe_id)
        result["escudo"] = from_str(self.escudo)
        result["faixa_classificacao"] = to_class(FaixaClassificacao, self.faixa_classificacao)
        result["faixa_classificacao_cor"] = from_union([from_none, lambda x: to_enum(Cor, x)], self.faixa_classificacao_cor)
        result["gols_contra"] = from_int(self.gols_contra)
        result["gols_pro"] = from_int(self.gols_pro)
        result["jogos"] = from_int(self.jogos)
        result["nome_popular"] = from_str(self.nome_popular)
        result["ordem"] = from_int(self.ordem)
        result["pontos"] = from_int(self.pontos)
        result["saldo_gols"] = from_int(self.saldo_gols)
        result["sigla"] = from_str(self.sigla)
        result["ultimos_jogos"] = from_list(lambda x: to_enum(UltimosJogo, x), self.ultimos_jogos)
        result["variacao"] = from_int(self.variacao)
        result["vitorias"] = from_int(self.vitorias)
        return result


class Edicao:
    data_fim: datetime
    data_inicio: datetime
    nome: str
    regulamento: str

    def __init__(self, data_fim: datetime, data_inicio: datetime, nome: str, regulamento: str) -> None:
        self.data_fim = data_fim
        self.data_inicio = data_inicio
        self.nome = nome
        self.regulamento = regulamento

    @staticmethod
    def from_dict(obj: Any) -> 'Edicao':
        assert isinstance(obj, dict)
        data_fim = from_datetime(obj["data_fim"])
        data_inicio = from_datetime(obj["data_inicio"])
        nome = from_str(obj["nome"])
        regulamento = from_str(obj["regulamento"])
        return Edicao(data_fim, data_inicio, nome, regulamento)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data_fim"] = self.data_fim.isoformat()
        result["data_inicio"] = self.data_inicio.isoformat()
        result["nome"] = from_str(self.nome)
        result["regulamento"] = from_str(self.regulamento)
        return result


class FaixasClassificacao:
    cor: Cor
    id: int
    nome: str

    def __init__(self, cor: Cor, id: int, nome: str) -> None:
        self.cor = cor
        self.id = id
        self.nome = nome

    @staticmethod
    def from_dict(obj: Any) -> 'FaixasClassificacao':
        assert isinstance(obj, dict)
        cor = Cor(obj["cor"])
        id = from_int(obj["id"])
        nome = from_str(obj["nome"])
        return FaixasClassificacao(cor, id, nome)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cor"] = to_enum(Cor, self.cor)
        result["id"] = from_int(self.id)
        result["nome"] = from_str(self.nome)
        return result


class Tipo:
    descricao: str
    tipo_id: int

    def __init__(self, descricao: str, tipo_id: int) -> None:
        self.descricao = descricao
        self.tipo_id = tipo_id

    @staticmethod
    def from_dict(obj: Any) -> 'Tipo':
        assert isinstance(obj, dict)
        descricao = from_str(obj["descricao"])
        tipo_id = int(from_str(obj["tipo_id"]))
        return Tipo(descricao, tipo_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["descricao"] = from_str(self.descricao)
        result["tipo_id"] = from_str(str(self.tipo_id))
        return result


class Fase:
    disclaimer: str
    slug: str
    tipo: Tipo

    def __init__(self, disclaimer: str, slug: str, tipo: Tipo) -> None:
        self.disclaimer = disclaimer
        self.slug = slug
        self.tipo = tipo

    @staticmethod
    def from_dict(obj: Any) -> 'Fase':
        assert isinstance(obj, dict)
        disclaimer = from_str(obj["disclaimer"])
        slug = from_str(obj["slug"])
        tipo = Tipo.from_dict(obj["tipo"])
        return Fase(disclaimer, slug, tipo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["disclaimer"] = from_str(self.disclaimer)
        result["slug"] = from_str(self.slug)
        result["tipo"] = to_class(Tipo, self.tipo)
        return result


class FasesNavegacao:
    atual: bool
    nome: str
    slug: str

    def __init__(self, atual: bool, nome: str, slug: str) -> None:
        self.atual = atual
        self.nome = nome
        self.slug = slug

    @staticmethod
    def from_dict(obj: Any) -> 'FasesNavegacao':
        assert isinstance(obj, dict)
        atual = from_bool(obj["atual"])
        nome = from_str(obj["nome"])
        slug = from_str(obj["slug"])
        return FasesNavegacao(atual, nome, slug)

    def to_dict(self) -> dict:
        result: dict = {}
        result["atual"] = from_bool(self.atual)
        result["nome"] = from_str(self.nome)
        result["slug"] = from_str(self.slug)
        return result


class Ante:
    escudo: str
    id: int
    nome_popular: str
    sigla: str

    def __init__(self, escudo: str, id: int, nome_popular: str, sigla: str) -> None:
        self.escudo = escudo
        self.id = id
        self.nome_popular = nome_popular
        self.sigla = sigla

    @staticmethod
    def from_dict(obj: Any) -> 'Ante':
        assert isinstance(obj, dict)
        escudo = from_str(obj["escudo"])
        id = from_int(obj["id"])
        nome_popular = from_str(obj["nome_popular"])
        sigla = from_str(obj["sigla"])
        return Ante(escudo, id, nome_popular, sigla)

    def to_dict(self) -> dict:
        result: dict = {}
        result["escudo"] = from_str(self.escudo)
        result["id"] = from_int(self.id)
        result["nome_popular"] = from_str(self.nome_popular)
        result["sigla"] = from_str(self.sigla)
        return result


class Equipes:
    mandante: Ante
    visitante: Ante

    def __init__(self, mandante: Ante, visitante: Ante) -> None:
        self.mandante = mandante
        self.visitante = visitante

    @staticmethod
    def from_dict(obj: Any) -> 'Equipes':
        assert isinstance(obj, dict)
        mandante = Ante.from_dict(obj["mandante"])
        visitante = Ante.from_dict(obj["visitante"])
        return Equipes(mandante, visitante)

    def to_dict(self) -> dict:
        result: dict = {}
        result["mandante"] = to_class(Ante, self.mandante)
        result["visitante"] = to_class(Ante, self.visitante)
        return result


class Sede:
    nome_popular: str

    def __init__(self, nome_popular: str) -> None:
        self.nome_popular = nome_popular

    @staticmethod
    def from_dict(obj: Any) -> 'Sede':
        assert isinstance(obj, dict)
        nome_popular = from_str(obj["nome_popular"])
        return Sede(nome_popular)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nome_popular"] = from_str(self.nome_popular)
        return result


class Transmissao:
    label: str
    url: str

    def __init__(self, label: str, url: str) -> None:
        self.label = label
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Transmissao':
        assert isinstance(obj, dict)
        label = from_str(obj["label"])
        url = from_str(obj["url"])
        return Transmissao(label, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["label"] = from_str(self.label)
        result["url"] = from_str(self.url)
        return result


class ListaJogo:
    data_realizacao: str
    equipes: Equipes
    hora_realizacao: str
    id: int
    placar_oficial_mandante: Optional[int]
    placar_oficial_visitante: Optional[int]
    placar_penaltis_mandante: None
    placar_penaltis_visitante: None
    sede: Sede
    transmissao: Optional[Transmissao]

    def __init__(self, data_realizacao: str, equipes: Equipes, hora_realizacao: str, id: int, placar_oficial_mandante: Optional[int], placar_oficial_visitante: Optional[int], placar_penaltis_mandante: None, placar_penaltis_visitante: None, sede: Sede, transmissao: Optional[Transmissao]) -> None:
        self.data_realizacao = data_realizacao
        self.equipes = equipes
        self.hora_realizacao = hora_realizacao
        self.id = id
        self.placar_oficial_mandante = placar_oficial_mandante
        self.placar_oficial_visitante = placar_oficial_visitante
        self.placar_penaltis_mandante = placar_penaltis_mandante
        self.placar_penaltis_visitante = placar_penaltis_visitante
        self.sede = sede
        self.transmissao = transmissao

    @staticmethod
    def from_dict(obj: Any) -> 'ListaJogo':
        assert isinstance(obj, dict)
        data_realizacao = from_str(obj["data_realizacao"])
        equipes = Equipes.from_dict(obj["equipes"])
        hora_realizacao = from_str(obj["hora_realizacao"])
        id = from_int(obj["id"])
        placar_oficial_mandante = from_union([from_int, from_none], obj["placar_oficial_mandante"])
        placar_oficial_visitante = from_union([from_int, from_none], obj["placar_oficial_visitante"])
        placar_penaltis_mandante = from_none(obj["placar_penaltis_mandante"])
        placar_penaltis_visitante = from_none(obj["placar_penaltis_visitante"])
        sede = Sede.from_dict(obj["sede"])
        transmissao = from_union([Transmissao.from_dict, from_none], obj["transmissao"])
        return ListaJogo(data_realizacao, equipes, hora_realizacao, id, placar_oficial_mandante, placar_oficial_visitante, placar_penaltis_mandante, placar_penaltis_visitante, sede, transmissao)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data_realizacao"] = from_str(self.data_realizacao)
        result["equipes"] = to_class(Equipes, self.equipes)
        result["hora_realizacao"] = from_str(self.hora_realizacao)
        result["id"] = from_int(self.id)
        result["placar_oficial_mandante"] = from_union([from_int, from_none], self.placar_oficial_mandante)
        result["placar_oficial_visitante"] = from_union([from_int, from_none], self.placar_oficial_visitante)
        result["placar_penaltis_mandante"] = from_none(self.placar_penaltis_mandante)
        result["placar_penaltis_visitante"] = from_none(self.placar_penaltis_visitante)
        result["sede"] = to_class(Sede, self.sede)
        result["transmissao"] = from_union([lambda x: to_class(Transmissao, x), from_none], self.transmissao)
        return result


class Rodada:
    atual: int
    ultima: int

    def __init__(self, atual: int, ultima: int) -> None:
        self.atual = atual
        self.ultima = ultima

    @staticmethod
    def from_dict(obj: Any) -> 'Rodada':
        assert isinstance(obj, dict)
        atual = from_int(obj["atual"])
        ultima = from_int(obj["ultima"])
        return Rodada(atual, ultima)

    def to_dict(self) -> dict:
        result: dict = {}
        result["atual"] = from_int(self.atual)
        result["ultima"] = from_int(self.ultima)
        return result


class Brasileirao:
    classificacao: List[Classificacao]
    edicao: Edicao
    faixas_classificacao: List[FaixasClassificacao]
    fase: Fase
    fases_navegacao: List[FasesNavegacao]
    lista_jogos: List[ListaJogo]
    lista_jogos_unica: bool
    lista_tipo_unica: bool
    rodada: Rodada
    artilheiros: List[Artilheiros]

    def __init__(self, classificacao: List[Classificacao], edicao: Edicao, faixas_classificacao: List[FaixasClassificacao], fase: Fase, fases_navegacao: List[FasesNavegacao], lista_jogos: List[ListaJogo], lista_jogos_unica: bool, lista_tipo_unica: bool, rodada: Rodada,artilheiros : List[Artilheiros]) -> None:
        self.classificacao = classificacao
        self.edicao = edicao
        self.faixas_classificacao = faixas_classificacao
        self.fase = fase
        self.fases_navegacao = fases_navegacao
        self.lista_jogos = lista_jogos
        self.lista_jogos_unica = lista_jogos_unica
        self.lista_tipo_unica = lista_tipo_unica
        self.rodada = rodada
        self.artilheiros = artilheiros

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome':
        assert isinstance(obj, dict)
        classificacao = from_list(Classificacao.from_dict, obj["classificacao"])
        edicao = Edicao.from_dict(obj["edicao"])
        faixas_classificacao = from_list(FaixasClassificacao.from_dict, obj["faixas_classificacao"])
        fase = Fase.from_dict(obj["fase"])
        fases_navegacao = from_list(FasesNavegacao.from_dict, obj["fases_navegacao"])
        lista_jogos = from_list(ListaJogo.from_dict, obj["lista_jogos"])
        lista_jogos_unica = from_bool(obj["lista_jogos_unica"])
        lista_tipo_unica = from_bool(obj["lista_tipo_unica"])
        rodada = Rodada.from_dict(obj["rodada"])
        artilheiros = from_list(Artilheiros.from_dict,obj["artilheiros"])
        return Brasileirao(classificacao, edicao, faixas_classificacao, fase, fases_navegacao, lista_jogos, lista_jogos_unica, lista_tipo_unica, rodada,artilheiros)

    def to_dict(self) -> dict:
        result: dict = {}
        result["classificacao"] = from_list(lambda x: to_class(Classificacao, x), self.classificacao)
        result["edicao"] = to_class(Edicao, self.edicao)
        result["faixas_classificacao"] = from_list(lambda x: to_class(FaixasClassificacao, x), self.faixas_classificacao)
        result["fase"] = to_class(Fase, self.fase)
        result["fases_navegacao"] = from_list(lambda x: to_class(FasesNavegacao, x), self.fases_navegacao)
        result["lista_jogos"] = from_list(lambda x: to_class(ListaJogo, x), self.lista_jogos)
        result["lista_jogos_unica"] = from_bool(self.lista_jogos_unica)
        result["lista_tipo_unica"] = from_bool(self.lista_tipo_unica)
        result["rodada"] = to_class(Rodada, self.rodada)
        result["artilheiros"] = from_list(lambda x: to_class(Artilheiros,x),self.artilheiros)
        return result


def brasileirao_from_dict(s: Any) -> Brasileirao:
    return Brasileirao.from_dict(s)


def brasileirao_to_dict(x: Brasileirao) -> Any:
    return to_class(Brasileirao, x)

import pandas
from fpdf import FPDF

df = pandas.read_csv("./data/DADOSSUS_ANIMAIS_PECONHENTOS2017.csv")
print(df.head(n=10))

quantidade_sexo = df.groupby(["Sexo"])["Sexo"].count().reset_index(name="Total")
print(quantidade_sexo.head())
quantidade_sexo_figure = quantidade_sexo.plot(x="Sexo", y="Total", kind="bar").get_figure()
quantidade_sexo_figure.show()
quantidade_sexo_figure.savefig('./data/quantidade_sexo.png')

quantidade_municipios = df.groupby(["Município de ocorrência do acidente"])[
    "Município de ocorrência do acidente"].count().reset_index(name="Ocorrências").query(
    "Ocorrências > 510").sort_values(by="Ocorrências", ascending=False)
print(quantidade_municipios.head())
quantidade_municipios_figure = quantidade_municipios.plot(x="Município de ocorrência do acidente", y="Ocorrências",
                                                          kind="bar").get_figure()
quantidade_municipios_figure.show()
quantidade_municipios_figure.savefig('./data/quantidade_municipios.png', bbox_inches='tight')

quantidade_profissao = df.groupby(["Ocupação"])["Ocupação"].count().reset_index(name="Total").sort_values(by='Total',
                                                                                                          ascending=False)
print(quantidade_profissao.head())
quantidade_profissao_figure = quantidade_profissao.query('Total > 200').plot(x="Ocupação", y="Total",
                                                                             kind="bar").get_figure()
quantidade_profissao_figure.show()
quantidade_profissao_figure.savefig('./data/quantidade_profissao.png', bbox_inches='tight')

pdf = FPDF()
pdf.add_page(orientation='L')
pdf.set_font('helvetica', size=12)
pdf.cell(txt="Animais Peçonhentos")
pdf.image('./data/quantidade_sexo.png', h=150, keep_aspect_ratio=True)
pdf.image('./data/quantidade_municipios.png', h=150, keep_aspect_ratio=True)
pdf.image('./data/quantidade_profissao.png', h=200, keep_aspect_ratio=True)
pdf.output("animais_peconhentos.pdf")

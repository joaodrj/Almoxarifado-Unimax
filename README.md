# Sistema de Gerenciamento de Estoque para Apoio aos Cursos de Engenharia e Arquitetura - Unimax

<p align="center">
   <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge" #vitrinedev/>
</p>

## Descrição do projeto
O Sistema de Gerenciamento de estoque para Apoio aos Cursos de Engenharia e Arquitetura da Faculdade Unimax é uma aplicação desenvolvida para auxiliar no controle e organização dos materiais e empréstimos utilizados pelos alunos desses cursos. O sistema foi projetado com o objetivo de facilitar o acesso e gerenciamento dos recursos disponíveis, tornando o processo mais eficiente e prático para os usuários.

# :hammer: Funcionalidades do projeto

- `Cadastro de alunos`: O sistema permite o cadastro dos alunos dos cursos de engenharia e arquitetura, incluindo informações como nome, RA (Registro Acadêmico) e semestre. Esses dados são armazenados em um banco de dados para consulta e uso posterior.
- `Controle de produtos`: É possível cadastrar os produtos disponíveis no almoxarifado, como materiais de construção, ferramentas, equipamentos, entre outros. Cada produto é identificado por um código de barras único, o que facilita a sua identificação e registro de empréstimos.
- `Empréstimos de produtos`: Os alunos podem solicitar empréstimos de produtos registrados no sistema. O sistema controla a quantidade disponível de cada item, evitando empréstimos em excesso ou de produtos não disponíveis. Além disso, o sistema registra as informações do aluno responsável pelo empréstimo, o produto solicitado e a quantidade emprestada.
- `Busca de produtos e alunos`: O sistema oferece a funcionalidade de busca, permitindo localizar rapidamente alunos e produtos cadastrados. Isso agiliza o processo de consulta e facilita a identificação de informações específicas.
- `Interface intuitiva`: O sistema conta com uma interface amigável e intuitiva, facilitando a navegação e uso por parte dos usuários. A disposição das informações, botões e menus foi pensada de forma a tornar a experiência do usuário agradável e eficiente.
## Objetivo
O objetivo principal do Sistema de Gerenciamento de Apoio aos Cursos de Engenharia e Arquitetura é proporcionar aos alunos e professores uma ferramenta que otimize o controle de materiais e empréstimos, garantindo um processo organizado e eficaz. Com o uso dessa aplicação, é possível reduzir o tempo gasto na busca por recursos, evitar perdas e extravios de materiais, e promover uma gestão mais eficiente dos recursos disponíveis.

Este projeto foi desenvolvido utilizando a linguagem de programação Python e frameworks como Tkinter para a interface gráfica. Além disso, foi utilizado um banco de dados para armazenamento das informações, garantindo a persistência dos dados.

Esperamos que este sistema seja uma ferramenta útil para a comunidade acadêmica da Faculdade Unimax, contribuindo para a organização e melhor aproveitamento dos recursos disponíveis nos cursos de engenharia e arquitetura.

## Capturas de Tela
Aqui estão algumas capturas de tela do sistema em funcionamento:
![Descrição do projeto GlicoCare, onde se tem um paciente medindo glicose com um glicosímetro, conectado via Bluetooth ao aplicativo que o profissional da saúde tem acesso.](https://github.com/joaodrj/Almoxarifado-Unimax/blob/main/imagens_capturaTela/login.png)
</p>

![Descrição do projeto GlicoCare, onde se tem um paciente medindo glicose com um glicosímetro, conectado via Bluetooth ao aplicativo que o profissional da saúde tem acesso.](https://github.com/joaodrj/Almoxarifado-Unimax/blob/main/imagens_capturaTela/telaInicial.png)
</p>

![Descrição do projeto GlicoCare, onde se tem um paciente medindo glicose com um glicosímetro, conectado via Bluetooth ao aplicativo que o profissional da saúde tem acesso.](https://github.com/joaodrj/Almoxarifado-Unimax/blob/main/imagens_capturaTela/telaEstoque.png)
</p>

![Descrição do projeto GlicoCare, onde se tem um paciente medindo glicose com um glicosímetro, conectado via Bluetooth ao aplicativo que o profissional da saúde tem acesso.](https://github.com/joaodrj/Almoxarifado-Unimax/blob/main/imagens_capturaTela/telaAlunos.png)
</p>

![Descrição do projeto GlicoCare, onde se tem um paciente medindo glicose com um glicosímetro, conectado via Bluetooth ao aplicativo que o profissional da saúde tem acesso.](https://github.com/joaodrj/Almoxarifado-Unimax/blob/main/imagens_capturaTela/telaSaida.png)
</p>

## Tecnologias utilizadas

Esta seção lista as principais tecnologias e bibliotecas utilizadas para desenvolver o projeto:



* [Python](https://www.python.org/) - Linguagem de programação utilizada para desenvolver o aplicativo.
* [Tkinter](https://docs.python.org/3/library/tkinter.html) -  Biblioteca padrão do Python para criação de interfaces gráficas.
* [SQLite3](https://docs.python.org/3/library/sqlite3.html) - Biblioteca Python para interagir com banco de dados SQLite

Make sure to replace the URLs with the correct links to the documentation or resources of each technology you are using in your project.



## :rocket: Rodando o projeto
## Explicação do projeto

O projeto é dividido em vários arquivos, cada um desempenhando uma função específica.

### `database.py`
Neste arquivo, estabelecemos a conexão com o banco de dados e criamos as tabelas necessárias para o funcionamento do sistema.

### `view.py`
No arquivo `view.py`, encontramos as funções responsáveis pela manipulação das tabelas no banco de dados. Aqui, realizamos operações como inserção, consulta, atualização e exclusão de dados.

### `login.py`
O arquivo `login.py` contém a implementação da tela de login do programa. É nesta tela que o usuário deve inserir seu login e senha para acessar o sistema. No momento, as credenciais de login padrão são "admin" para o nome de usuário e "admin" para a senha.

### `home.py`
O arquivo `home.py` contém a estrutura principal do programa. Nele, definimos classes para cada tela do programa, incluindo a tela principal e outras telas auxiliares. Essas classes são responsáveis por exibir as informações relevantes ao usuário e permitir a interação com o sistema.

### `main.py`
O arquivo `main.py` é o ponto de entrada do programa. É neste arquivo que chamamos as funções e classes necessárias para iniciar e executar o programa.

Essa estrutura de arquivos e módulos permite uma organização clara e modular do projeto, facilitando a manutenção e o desenvolvimento de novos recursos. Cada arquivo desempenha um papel específico, contribuindo para a funcionalidade geral do sistema.

## Passos iniciais

Para executar o projeto, siga os passos abaixo:

1. Instale o Python: [https://www.python.org/](https://www.python.org/)

2. Adicione o diretório do Pip (gerenciador de pacotes do Python) às variáveis de ambiente do Windows. Caso não tenha o Pip instalado, visite o site [https://pypi.org/project/pip/](https://pypi.org/project/pip/) e instale o pacote, que é usado para facilitar a instalação de bibliotecas do Python.

3. Abra a pasta contendo os arquivos em uma IDE de sua preferência. Para este projeto, estamos usando o VS Code.

4. Instale as bibliotecas necessárias para executar o projeto. No arquivo `requirements.txt`, encontram-se as bibliotecas utilizadas. Para instalá-las, execute o seguinte comando no terminal:

   ```shell
   pip install -r requirements.txt
   
5. Execute o arquivo main.py para testar o programa.



## :soon: Implementação futura

Aqui estão algumas implementações futuras que podem ser adicionadas ao projeto para o correto funcionamento :

1. **Movimentação de Estoque para Empréstimos**: Implementar a funcionalidade de registrar empréstimos de materiais aos alunos, permitindo a movimentação do estoque. Isso inclui a atualização do banco de dados para registrar empréstimos, a criação de telas para gerenciar empréstimos e a verificação de disponibilidade de materiais.

2. **Relatórios e Estatísticas**: Adicionar recursos de geração de relatórios e estatísticas para fornecer insights sobre o estoque, empréstimos, devoluções, etc. Isso pode incluir a criação de gráficos, tabelas e visualizações para facilitar a compreensão dos dados.

3. **Integração com API de Notificações**: Integrar uma API de notificações para enviar lembretes e notificações aos alunos sobre a data de devolução dos materiais emprestados. Isso pode ser feito por meio de mensagens de texto, e-mails ou notificações no aplicativo.

4. **Melhorias na Interface do Usuário**: Aprimorar a interface do usuário com elementos visuais, melhor organização dos componentes e fluxo de navegação intuitivo. Isso pode incluir o uso de bibliotecas de design como Bootstrap, Material-UI, entre outras.

5. **Gerenciamento de Usuários**: Implementar um sistema de autenticação e controle de acesso para diferentes usuários, como administradores e alunos. Isso permite a criação de contas de usuário, login seguro e permissões de acesso adequadas.

Essas são apenas algumas sugestões de melhorias para o projeto. Sinta-se à vontade para adicionar outras funcionalidades de acordo com suas necessidades e objetivos.



## :handshake: Autores
<table>
  <tr>
    <td align="center">
      <a href="http://github.com/joaodrj">
        <img src="https://avatars.githubusercontent.com/u/62823813?s=400&u=9701c862c3511636ce79d721359fa49f3560dff1&v=4" width="100px;" alt="Foto de João no GitHub"/><br>
        <sub>
          <b>João Jr</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE.md para mais informações.


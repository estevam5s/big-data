# # from client.src.pages.👻_Login import login_page
# from client.src.pages.login import *
# import streamlit as st
# # import client.setup as setup
# import plotly.express as px


# if __name__ == '__main__':
#   df = px.data.iris()

#   if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

#   if not st.session_state.logged_in:
#     logged_in = login_page()

#     if logged_in:
#         st.session_state.logged_in = True
#         st.experimental_rerun()
#   else:
#     st.empty()
#     # setup.mainLogin()
#     if st.button("Logout"):
#       st.session_state.logged_in = False
#       st.experimental_rerun()
      
      

# from client.src.pages.👻_Login import login_page
# from client.src.pages.login import *
import streamlit as st
import client.setup as setup
import plotly.express as px


import streamlit as st
from PIL import Image
from streamlit_extras.let_it_rain import rain


logo_img = Image.open('client/src/public/if-logo.png')

# Caminho para o arquivo .txt com os dados de login
USERS_FILE = 'usuarios.txt'  # O arquivo .txt onde os usuários estão armazenados

# Função para ler os usuários e senhas do arquivo .txt
def read_users_from_file():
    users = {}
    try:
        with open(USERS_FILE, 'r') as file:
            for line in file.readlines():
                line = line.strip()  # Remove espaços em branco no início e no final
                if line:  # Ignora linhas vazias
                    if ',' in line:  # Verifica se a linha contém uma vírgula para dividir
                        try:
                            username, password = line.split(',')
                            users[username] = password
                        except ValueError:
                            st.warning(f"Formato inválido na linha: '{line}'. Ignorando...")
                    else:
                        st.warning(f"Formato inválido na linha: '{line}'. Esperava-se uma vírgula para separar usuário e senha.")
    except FileNotFoundError:
        st.error(f"O arquivo {USERS_FILE} não foi encontrado.")
    return users


# Função de autenticação
def authenticate_user(username, password):
    users = read_users_from_file()  # Lê os usuários do arquivo
    if username in users:
        if users[username] == password:
            return True
        else:
            st.error("Senha incorreta.")
            return False
    else:
        st.error("Nome de usuário não encontrado.")
        return False

def login_page():
    rain(
        emoji="🎃",
        font_size=45,
        falling_speed=12,
        animation_length="infinite",
    )
    opcao = st.radio("Escolha uma opção:", ("Fazer login"))

    if opcao == "Fazer login":
        if 'logged_in' not in st.session_state:
            st.session_state.logged_in = False

        st.image(logo_img, use_column_width=True)
        username = st.text_input("Nome de usuário", key="username_input")
        password = st.text_input("Senha", type="password", key="password_input")

        if st.button("Login"):
            if authenticate_user(username, password):
                st.session_state.logged_in = True
                with st.spinner("Carregando..."):
                    st.success("Login efetuado com sucesso!")
                    from time import sleep
                    from stqdm import stqdm

                    for _ in stqdm(range(50), desc="configurando o servidor", mininterval=1):
                        sleep(0.1)

                    st.balloons()

                return True
            else:
                if username == "" and password == "":
                    st.error("Por favor, insira um nome de usuário e senha.")
                st.info("Se você esqueceu sua senha, entre em contato com o administrador.")
                st.markdown("""
                <style>
                    .container {
                      display: flex;
                      flex-direction: column;
                      align-items: center;
                      justify-content: center;
                      padding: 2rem;
                    }

                    .form-group {
                      width: 100%;
                      margin-bottom: 1rem;
                    }

                    .form-control {
                      width: 100%;
                      padding: 0.75rem;
                      font-size: 1rem;
                      border-radius: 0.25rem;
                      border: 1px solid #ced4da;
                    }

                    .form-control:focus {
                      outline: none;
                      box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
                      border-color: #80bdff;
                    }

                    .btn {
                      display: inline-block;
                      font-weight: 400;
                      color: #212529;
                      text-align: center;
                      vertical-align: middle;
                      user-select: none;
                      background-color: transparent;
                      border: 1px solid transparent;
                      padding: 0.375rem 0.75rem;
                      font-size: 1rem;
                      line-height: 1.5;
                      border-radius: 0.25rem;
                      transition: color 0.15s ease-in-out,
                                  background-color 0.15s ease-in-out,
                                  border-color 0.15s ease-in-out,
                                  box-shadow 0.15s ease-in-out;
                    }

                    .btn-primary {
                        color: #fff;
                        background-color: #007bff;
                        border-color: #007bff;
                    }

                    .btn-primary:hover {
                        color: #fff;
                        background-color: #0069d9;
                        border-color: #0062cc;
                    }

                    .btn-primary:focus {
                        color: #fff;
                        background-color: #0069d9;
                        border-color: #0062cc;
                        box-shadow: 0 0 0 0.2rem rgba(38, 143, 255, 0.5);
                    }
                </style>
                """, unsafe_allow_html=True)

                st.header("Contact")

                contact_form = """
                  <div class="container">
                    <form id="contact-form" action="https://formsubmit.co/{}" method="POST">
                      <div class="form-group">
                        <input class="form-control" type="text" name="name" placeholder="Your name" required>
                      </div>
                      <div class="form-group">
                        <input class="form-control" type="email" name="email" placeholder="Your email" required>
                      </div>
                      <div class="form-group">
                        <textarea class="form-control" name="message" placeholder="Your message here"></textarea>
                      </div>
                      <div class="form-group">
                        <button class="btn btn-primary" type="submit" onclick="validateForm(event)">Send</button>
                      </div>
                    </form>
                  </div>
                  """.format("estevamsouzalaureth@gmail.com")  # Substitua o endereço de e-mail aqui

                javascript_code = """
                  <script>
                    function validateForm(event) {
                      var form = document.getElementById('contact-form');
                      var nameInput = form.elements['name'];
                      var emailInput = form.elements['email'];
                      var messageInput = form.elements['message'];

                      if (nameInput.value.trim() === '' || emailInput.value.trim() === '' || messageInput.value.trim() === '') {
                          event.preventDefault();
                          alert('Por favor, preencha todos os campos do formulário.');
                      } else {
                          animateSubmitButton();
                      }
                    }

                    function animateSubmitButton() {
                      var submitButton = document.querySelector('.btn-primary');
                      submitButton.innerHTML = 'Sending...';
                      submitButton.classList.add('animate__animated', 'animate__fadeOut');

                      setTimeout(function() {
                          submitButton.innerHTML = 'Sent!';
                          submitButton.classList.remove('animate__fadeOut');
                          submitButton.classList.add('animate__zoomIn');
                      }, 2000);
                    }
                  </script>
                  """

                st.markdown(contact_form + javascript_code, unsafe_allow_html=True)

        return False
  
    else:
        from .criar_conta import criar_conta
        st.image(logo_img, use_column_width=True)
        return criar_conta()



if __name__ == '__main__':
    df = px.data.iris()

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        logged_in = login_page()

        if logged_in:
            st.session_state.logged_in = True
            st.rerun()  # Substituído experimental_rerun por rerun
    else:
        st.empty()
        setup.mainLogin()
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()  # Substituído experimental_rerun por rerun

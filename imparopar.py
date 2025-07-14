import streamlit as st
from random import randint
from time import sleep
st.title('Par ou Ímpar')



if 'vitoria' not in st.session_state:
    st.session_state.vitoria = 0
if 'derrota' not in st.session_state:
    st.session_state.derrota = 0
if 'rodada' not in st.session_state:
    st.session_state.rodada = 0
opcoes = ['Par', 'Ímpar']
jogador = st.selectbox('Escolha Par ou Ímpar', opcoes)
valor_jogador = st.number_input('Numero',min_value=0, max_value=10)

valor_computador = randint(0,10)
valor_final = valor_jogador + valor_computador

if valor_final % 2 == 0:
    rodada = 'PAR'
else:
    rodada = 'ÍMPAR'
if st.button('Jogar'):

    st.write('-' * 20)
    st.write(f'O jogador jogou {valor_jogador} e o computador {valor_computador} soma =  {valor_final}')
    st.write('-' * 20)
    st.write(f'DEU {rodada}')

    if rodada == 'PAR' and jogador == 'Par' or \
        rodada == 'Ímpar' and jogador == 'Ímpar':
        st.success(f'O Jogador venceu')
        st.session_state.vitoria += 1
    else:
        st.error('O computador ganhou')
        st.session_state.derrota += 1
    st.session_state.rodada += 1
st.sidebar.title('Rodadas')
if st.sidebar.button('Resetar'):
    st.session_state.derrota = 0
    st.session_state.vitoria = 0
    st.session_state.rodada = 0
st.sidebar.warning(f'Rodadas: {st.session_state.rodada}')
st.sidebar.success(f'Vitorias: {st.session_state.vitoria}')
st.sidebar.error(f'Derrotas: {st.session_state.derrota}')

import streamlit as st
import functions

todos = functions.read_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo app")
st.subheader("This is my Todo App.")
st.write("This is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",
              label_visibility="hidden",
              placeholder="Add a Todo",
              on_change=add_todo,
              key='new_todo')





st.session_state

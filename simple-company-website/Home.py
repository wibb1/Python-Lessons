import streamlit as st
import pandas


def show_person(name, role, image_url):
    st.subheader(name)
    st.write(role)
    st.image('images/' + image_url)


def get_person_data(row):
    return {
        'name': f"{row['first name'].title()} {row['last name'].title()}",
        'role': row['role'].title(),
        'image_url': row['image']
    }


st.set_page_config(layout='wide')

st.header("The Best Company")

company_description = """
Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis
obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam
nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,
tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit,
quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos 
sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
recusandae alias error harum maxime adipisci amet laborum. Perspiciatis 
minima nesciunt dolorem! Officiis iure rerum voluptates a cumque velit 
quibusdam sed amet tempora. Sit laborum ab, eius fugit doloribus tenetur 
fugiat, temporibus enim commodi iusto libero magni deleniti quod quam 
consequuntur! Commodi minima excepturi repudiandae velit hic maxime
doloremque. Quaerat provident commodi consectetur veniam similique ad 
earum omnis ipsum saepe, voluptas, hic voluptates pariatur est explicabo 
fugiat, dolorum eligendi quam cupiditate excepturi mollitia maiores labore 
suscipit quas? Nulla, placeat. Voluptatem quaerat non architecto ab laudantium
modi minima sunt esse temporibus sint culpa, recusandae aliquam numquam 
totam ratione voluptas quod exercitationem fuga. Possimus quis earum veniam 
quasi aliquam eligendi, placeat qui corporis!
"""
st.write(company_description)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('data.csv')

with col1:
    for index, row, in df[:4].iterrows():
        pd = get_person_data(row)
        show_person(pd['name'], pd['role'], pd['image_url'])

with col2:
    for index, row, in df[4:8].iterrows():
        pd = get_person_data(row)
        show_person(pd['name'], pd['role'], pd['image_url'])

with col3:
    for index, row, in df[8:].iterrows():
        pd = get_person_data(row)
        show_person(pd['name'], pd['role'], pd['image_url'])

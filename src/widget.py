from PIL import Image
import io 

import streamlit as st
import numpy as np

from src import code

def view():
    st.title('Widgets')

    # import
    st.header('Import streamlit')
    st.code("""import streamlit as st""", language='python')

    # checkbox
    st.header('Checkbox')
    col1, col2 = st.columns(2)
    with col1:
        checkbox_state = st.checkbox('Show text')
        if checkbox_state:
            st.write('checkbox enable')

    with col2:
        st.code(code.WIDGET_CHECKBOX, language='python')

    # button
    st.header('Button')
    col1, col2 = st.columns(2)
    with col1:
        button_state = st.button('Say hello')
        if button_state:
            st.write('Why hello there')
        else:
            st.write('Goodbye')
    
    with col2:
        st.code(code.WIDGET_BUTTON, language='python')

    # selectbox
    st.header('Selectbox')
    col1, col2 = st.columns(2)
    with col1:
        option = st.selectbox(
            'select box:',
            [1, 2, 3]
        )
        st.write('You selected: ', option)
    
    with col2:
        st.code(code.WIDGET_SELECTBOX, language='python')

    # inputbox
    st.header('Inputbox')
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input('inputbox', 'hello')
        st.write('inputbox:', title)
    
    with col2:
        st.code(code.WIDGET_INPUT, language='python')

    # file upload
    st.header('File uploader')
    col1, col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader('Choose a image file')
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            img_array = np.array(image)
            st.image(
                image, caption='upload images',
                use_column_width=True
            )
    
    with col2:
        st.code(code.WIDGET_FILEUPLOADER, language='python')

    # Expander
    st.header('Expander (New in 0.86.0)')
    col1, col2 = st.columns(2)
    with col1:
        with st.expander('See detail'):
            st.write('Hello expander!')

    with col2:
        st.code(code.WIDGET_EXPANDER, language='python')

    # Download button
    st.header('Download button (New in 0.88.0)')
    col1, col2 = st.columns(2)
    with col1:
        binary_contents = b'example content'
        st.download_button('Download binary file', binary_contents)

    with col2:
        st.code(code.WIDGET_DOWNLOAD, language='python')


if __name__ == '__main__':
    view()

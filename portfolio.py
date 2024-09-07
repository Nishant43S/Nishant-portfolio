import streamlit as st
from streamlit_option_menu import option_menu
import base64
import time
import streamlit.components.v1 as components

######  functions

@st.cache_data
def insert_css(css_file):  ## insert external css function
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

@st.cache_data
def insert_html(html_file):  ## insert external html function
    with open(html_file) as f:
        st.markdown(f.read(),unsafe_allow_html=True)



st.set_page_config(  ### page settings
    page_title="Nishant Maity",
    page_icon="👑",
    initial_sidebar_state="collapsed",
    layout="wide"
)

######  background music

def play_music(html_music_file):
    with open(html_music_file) as f:
        return f.read()

background_music1 = play_music("background-music.html")



if __name__=="__main__":
    insert_css("cssfiles/body.css") ## inserting body css

Side_bar = st.sidebar

with Side_bar:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    Main_menu = option_menu(
        menu_title="",
        options=["About","Certificates","Achievements","Internships"],
        icons=["person","patch-check","trophy","card-text"]
    )


st.logo("assets/namelogo.png")

if Main_menu=="About": ###### home page
    id_col1 , id_col2 = st.columns(2)

    with id_col1:
        st.text("")
        st.text("")
        st.text("")
        # Path to your image file
        image_path = "assets/nishant_pic.jpg"  # Replace with your image file path

        # Read the image file and encode it in base64
        with open(image_path, "rb") as img_file:
            img_data = img_file.read()
            img_base64 = base64.b64encode(img_data).decode()

        # Define the HTML code with the base64 image
        html_code = f'''
        <div class="photo-container">
            <img src="data:image/jpeg;base64,{img_base64}" alt="Photo" class="photo" style="width:100%;">
        </div>
        '''

        # Display the HTML in Streamlit
        st.markdown(html_code, unsafe_allow_html=True)

        if __name__=="__main__":  ### profile css
            insert_css("cssfiles/pic.css")


    with id_col2:
        st.text("")
        st.text("")
        st.text("")
     
        if __name__=="__main__": ###  inserting name html file
            insert_html("name.html")

        
        about_me = """
                I'm Nishant Maity, a skilled Python programmer specializing in generative AI. I'm excited about learning new technologies and aiming to become an expert in this ever-changing field.
                 """
        
        def stream_aboutme():  ### about me
            for word in about_me.split(" "):
                yield word + " "
                time.sleep(0.02)
        st.write_stream(stream_aboutme)

       

        pdf_file_path = "assets/NishantCV.pdf"  # Cv file

        # Read the PDF file in binary mode and encode it to Base64
        with open(pdf_file_path, "rb") as file:
            pdf_data = file.read()
            b64_pdf = base64.b64encode(pdf_data).decode()

        # Create a download button using HTML and Base64
        download_button_html = f"""
        <a href="data:application/pdf;base64,{b64_pdf}" download="NishantCV.pdf">
            <button class="neon-button">Download Cv</button>
        </a>
        """

        # Display the button using st.markdown
        st.markdown(download_button_html, unsafe_allow_html=True)

        if __name__=="__main__": ### name css
            insert_css("cssfiles/name.css")

        st.text("")
        st.text("")

        ## progress bars

        Progress_bar1 , Progress_bar2 = st.columns([2,2],gap="large")

        with Progress_bar1:

            coding_skill = st.progress(0)  ### coding skills
            for i in range(91):
                time.sleep(0.002)
                coding_skill.progress(i+1,text="91%")

            st.markdown("<div class='Bar-text'>Coding Skills</div>",unsafe_allow_html=True)

            st.text("")
            st.text("")

            problem_solving = st.progress(0)  ### poblem solving
            for i in range(73):
                time.sleep(0.002)
                problem_solving.progress(i+1,text="73%")

            st.markdown("<div class='Bar-text'>Problem Solving</div>",unsafe_allow_html=True)

        with Progress_bar2:

            coding_skill = st.progress(0)  ### team work
            for i in range(64):
                time.sleep(0.004)
                coding_skill.progress(i+1,text="64%")

            st.markdown("<div class='Bar-text'>Team Work</div>",unsafe_allow_html=True)

            st.text("")
            st.text("")

            problem_solving = st.progress(0)  ### Analytical skills
            for i in range(78):
                time.sleep(0.003)
                problem_solving.progress(i+1,text="78%")

            st.markdown("<div class='Bar-text'>Analytical Skills</div>",unsafe_allow_html=True)


            if __name__=="__main__": ### progress bar css
                insert_css("cssfiles/progressbar.css")

            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            if __name__=="__main__":
                components.html(background_music1,height=0)
            
            
################################################################################

##  recent work
    st.markdown("<h1 class='recent-work block'>Recent Work</h1>",
         unsafe_allow_html=True
        )

    st.text("")
    st.text("")
    st.text("")

    
    blanck_recent1 , Recent_work1 , Recent_work2 , blanck_recent2= st.columns([1,6,6,1],gap="large")

    with blanck_recent1:
        pass
       


    with Recent_work1:

        st.markdown(
            """
            <div class="box block" style=" float: left;">
            <div class="block">
                <h3 class="h3-heading">Wikipedia article scrapper</h3>
                <p>it is used to scrap the wikipedia articles it is made with python. it is responsive and it is hosted on python streamlit. you can download articles in the txt format. it is web app.</p>
                <h3 class="h3-heading">Languages</h3>
                <ul class="list" type="none">
                    <li>Python</li>
                    <li>HTML5</li>
                    <li>CSS3</li>
                    <li>Bootstrap</li>
                </ul>
                <span><a target="_main" href="https://wikisearch-article-scraper-nishant-maity.streamlit.app/" style="text-decoration: none; ">view project</a></span>
                <span style="margin-left: 25px;"><a target="_main" href="https://github.com/Nishant43S/wikisearch-article-scraper.git" style="text-decoration: none; ">github</a></span>
            </div>
            </div>
            """,unsafe_allow_html=True
        )
        
        
        st.markdown(
            """
            <div class="box block" style="margin-top: 73px; float: left;">
            <div class="block">
                <h3 class="h3-heading">Automation App</h3>
                <p>It has multiple automation features like message spammer, phone N.o information, email sender,whatapp spammer,python module downloade, etc. It is a desktop application</p>
                <h3 class="h3-heading">Languages & Libraies</h3>
                <ul class="list" type="none">
                    <li>Python</li>
                    <li>tkbootstrap,tkinter - Gui</li>
                    <li>pyautogui, pywhatkit - Automation</li>
                    <li>SMTP - Email</li>
                </ul>
                <span><a target="_main" href="#" style="text-decoration: none; "></a></span>
                <span style="margin-left: 0px;"><a target="_main" href="https://github.com/Nishant43S/automation-app.git" style="text-decoration: none; ">github</a></span>
            </div>
            </div>
            """,unsafe_allow_html=True
        )



    with Recent_work2:

        st.markdown(
            """
            <div class="box block" style="float: right;">
            <div class="block">
                <h3 class="h3-heading">Seo Image Finder</h3>
                <p>it is used to find the seo friendly images , gifs ,etc it is made with python.it is hosted on python streamlit. you can download images and use them into your blogs , yt videos,etc. it is web app.</p>
                <h3 class="h3-heading">Languages & Libraries</h3>
                <ul class="list" type="none">
                    <li>Python</li>
                    <li>HTML5</li>
                    <li>CSS3</li>
                    <li>Streamlit, Base64, PIL</li>
                </ul>
                <span><a target="_main" href="https://seo-image-finder-nishant-maity.streamlit.app/"  style="text-decoration: none; " >view project</a></span>
                <span style="margin-left: 25px;"><a target="_main" href="https://github.com/Nishant43S/Seo-Image-finder.git" style="text-decoration: none; ">github</a></span>
            </div>
            </div>
            """,unsafe_allow_html=True
        )



        st.markdown(
            """
            <div class="box block" style="margin-top: 73px; float: right;">
            <div class="block">
                <h3 class="h3-heading">File Finder</h3>
                <p>it is web scraping poject used to find the files like pdf, csv, pptx, docs,etc. it is made with python.it is hosted on python streamlit. you can find the exact links of files. it is web app.</p>
                <h3 class="h3-heading">Languages & Libraries</h3>
                <ul class="list" type="none">
                    <li>Python</li>
                    <li>HTML5</li>
                    <li>Bootstrap - icons</li>
                    <li>Streamlit, Google-search</li>
                </ul>
                <span><a target="_main" href="https://file-searcher-nishant-maity.streamlit.app/" style="text-decoration: none; " >view project</a></span>
                <span style="margin-left: 25px;"><a target="_main" href="https://github.com/Nishant43S/File-Searcher-webApp.git" style="text-decoration: none; ">github</a></span>
            </div>
            </div>
            """,unsafe_allow_html=True
        )


    with blanck_recent2:
        pass
       

    if __name__=="__main__": ### recent work css
        insert_css("cssfiles/recent-work.css")

    st.text("")
    st.text("")
    st.text("")
    
   

    ##############    about me   ##########

    st.markdown("<h1 class='About-me block'>About Me </h1>",
            unsafe_allow_html=True
    )
    st.text("")
    st.text("")

    about_me , professional_skills ,blank_aboutme = st.columns([6,3,1],gap="small")

    with about_me:
        if __name__=="__main__":
            insert_html("about-me.html")

    with professional_skills:
        st.text("")
        st.markdown("<h2 class='block' style='color: #7dd87d; cursor: pointer;'>Professional Skills</h2>",
                    unsafe_allow_html=True)
        st.text("")
        st.info("Python Specialist")
        st.success("Generative Ai Developer")
        st.info("Web & Desktop Application Developer")
        st.success("Ml Developer")

    with blank_aboutme:
        pass

    st.text("")
    st.text("")
    st.text("")
    st.text("")
    

    blank_skill1 , skill_slider ,blank_skill2 = st.columns([1,7,1])

    with blank_skill1:
        pass
    with blank_skill2:
        pass

        ############  skills infinite slide animation

    with skill_slider:

        @st.cache_data
        def Skills_scroll(Html_file):
            with open(Html_file) as f:
                return f.read()
        Skill_animation = Skills_scroll("aboutme-skills.html")
        components.html(Skill_animation,height=100)
        
       

    if __name__=="__main__": ### about me css
        insert_css("cssfiles/about-me.css")

    st.text("")
    st.text("")
    st.text("")

    ###########  contact me ###########

    st.markdown("<h1 style='text-align: center;'>Contact Me</h1>",
            unsafe_allow_html=True)


    st.text("")
    st.text("")

    c1 , contact_me_form , social_links , c2 = st.columns([1,5,5,1],gap="medium")

    with c1:
        pass
    with c2:
        pass

    with contact_me_form:

        # @st.cache_data
        def contactMe(Contact_form):  ### contact me page location
            with open(Contact_form) as f:
                return f.read()
            
        Contact_form = contactMe("contact-me.html")
        components.html(Contact_form,height=560)


    with social_links:
        st.markdown("<h3 style='text-align:center;></h3>",unsafe_allow_html=True)
        st.text("")
        st.text("")
        

        st.markdown("<h4>Stay Connected!</h4>",unsafe_allow_html=True)
        st.markdown(
            """
                <p>
                 Follow me on my social media platforms to stay updated with my latest projects, insights, and innovations in AI, machine learning, and technology
                </p>
            """,unsafe_allow_html=True
        )


        if __name__=="__main__":
            insert_html("socialmedia-links.html")

        
if Main_menu == "Achievements":   ######3 achievments

    st.markdown("""
        <h1 class='achievements-title drop-animation' style='text-align: center; margin: 0;'>Achievements</h1>
                """,
    unsafe_allow_html=True)
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    
    if __name__=="__main__":  ### achievements html
        insert_html("achievements.html")

    if __name__=="__main__": ### achievements css
        insert_css("cssfiles/achievements.css")

@st.cache_data()
def Show_Certficate(path):  ### certificate function
    st.image(
        image=f"Certificates/{path}",
        use_column_width=True
    )

if Main_menu == "Certificates":
    st.markdown("""
        <h1 class='Certificates-title drop-animation' style='text-align: center; margin: 0;'>Certificates</h1>
                """,
    unsafe_allow_html=True)
    st.text("")
    


    Certficate_col1 , Certficate_col2 = st.columns(2,gap="large")

    with Certficate_col1:  ############  certificate column 1
        st.subheader("Core Java")
        Show_Certficate("java.png")

        st.text("")
        st.text("")

        st.subheader("Introduction to HTML5")
        Show_Certficate("html5.jpg")

        st.text("")
        st.text("")
        
        st.subheader("Data Analysis Using Python")
        Show_Certficate("data_analysis_python.jpeg")

        st.text("")
        st.text("")

        st.subheader("Tkinter Python")
        Show_Certficate("tkinter_python.jpg")

        st.text("")
        st.text("")

        st.subheader("C programing")
        Show_Certficate("C_basic.jpg")

        st.text("")
        st.text("")

        st.subheader("Beautifil Soup")
        Show_Certficate("Bs4.jpg")

        st.text("")
        st.text("")

        st.subheader("Canva")
        Show_Certficate("canva.jpg")

        st.text("")
        st.text("")

    with Certficate_col2:  ###########  certificate column 2
        
        st.subheader("Statistics Using Python")
        Show_Certficate("statstics_using_py.jpeg")

        st.text("")
        st.text("")

        st.subheader("R programing for Data Science")
        Show_Certficate("r.jpeg")

        st.text("")
        st.text("")

        st.subheader("Python Programing & Data science")
        Show_Certficate("py_dataScience.png")

        st.text("")
        st.text("")

        st.subheader("Python Pandas")
        Show_Certficate("py_pandas.jpg")

        st.text("")
        st.text("")

        st.subheader("Streamlit Tutorial")
        Show_Certficate("streamlit.jpg")

        st.text("")
        st.text("")

        st.subheader("CSS Tutorial")
        Show_Certficate("css_tutorial.jpg")

        st.text("")
        st.text("")

        st.subheader("Ai Data Science & Data Analysis")
        Show_Certficate("ai_data_science.jpeg")

        st.text("")
        st.text("")

    if __name__=="__main__": ### certificate css
        insert_css("cssfiles/Certificates.css")

if Main_menu == "Internships":  ###### internships
    st.markdown("""
        <h1 class='internship-title drop-animation' style='text-align: center; margin: 0;'>Internships</h1>
                """,
    unsafe_allow_html=True)
    st.text("")
    st.text("")
    st.text("")

    Accenture_internship , acc_certificate = st.columns([7,4],gap="large")

    with Accenture_internship: ######### Accenture internship

        if __name__=="__main__":  #### html file
            insert_html("Internships/Accenture.html")

        if __name__=="__main__": ###  css
            insert_css("cssfiles/internship.css")

    with acc_certificate:
        st.text("")
        st.text("")
        st.text("")
        st.image(image="internship_certificates/Accenture_datascience.jpg",use_column_width=True)

    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    Genai_internship , genai_certificate = st.columns([7,4],gap="large")

    with Genai_internship: ######### generative internship

        if __name__=="__main__":  #### html file
            insert_html("Internships/Bcg_genai.html")

        if __name__=="__main__": ###  css
            insert_css("cssfiles/internship.css")

    with genai_certificate:
        st.text("")
        st.text("")
        st.text("")
        st.image(image="internship_certificates/genai.jpg",use_column_width=True)

    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    Datascience_internship , Datascience_certificate = st.columns([7,4],gap="large")

    with Datascience_internship: ######### datascience internship

        if __name__=="__main__":  #### html file
            insert_html("Internships/Bcg_datascience.html")

        if __name__=="__main__": ###  css
            insert_css("cssfiles/internship.css")

    with Datascience_certificate:
        st.text("")
        st.text("")
        st.text("")
        st.image(image="internship_certificates/bcg_datascience.jpg",use_column_width=True)

    



if __name__=="__main__":
    insert_css("cssfiles/animation.css")
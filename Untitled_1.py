import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import wordcloud
from wordcloud.wordcloud import STOPWORDS
import plotly.express as px #pip install
from plotly.subplots import make_subplots
import plotly.graph_objects as go




#Importing data
@st.cache
def get_data():
    return pd.read_excel("/Volumes/GoogleDrive/My Drive/Rysense/28-08-2021/Codes/RS_3_5_PartC.xlsx")

data=get_data()
#Create a text element and let the reader know the data is loading.
data_load_state=st.text('Loading data...')
data_load_state.text('Loading data...done!')

@st.cache
def get_data1():
    return pd.read_excel("/Volumes/GoogleDrive/My Drive/Rysense/28-08-2021/Codes/RS_3_5_keywords_PartC.xlsx")

data1=get_data1()



st.title('Rysense BTO Survey response analysis')


# TOPICS
st.sidebar.checkbox("Show Housing Profiles by Topic")
select = st.sidebar.selectbox('Select a Topic',data['DOMINANT_TOPIC'])
#get the TOPIC selected in the selectbox
state_data = data[data['DOMINANT_TOPIC'] == select]
select_status = st.sidebar.radio("Housing Profiles of Respondents", ('Settled Homeowner',
'2nd Timer', '1st Timer', 'Others'))

#Plotting the graph
"""
def get_total_dataframe(dataset):
    total_dataframe=pd.DataFrame({
    'Housing Profile of Respondents':['Settled Homeowner','2nd Timer','1st Timer','Others'],
    'Number of cases':(dataset.iloc[0]['Settled Homeowner'],
    dataset.iloc[0]['2nd Timer'],
    dataset.iloc[0]['1st Timer'],
    dataset.iloc[0]['Others'])})
    return total_dataframe

state_total=get_total_dataframe(state_data)

if st.sidebar.checkbox("Show analysis by Topic",True,key=2):
    st.markdown("## **Topic level analysis**")
    st.markdown("### Overall Settled Homeowner,2nd Timer,1st Timer and Others cases in %s yet" %(select))
    if not st.checkbox('Hide Graph',False,key=1):
        state_total_graph=px.bar(
        state_total,
        x='Housing Profiles',
        y='Number of Topics',
        labels={'Number of Profile':'Number of cases in %s'%(select)},
        color='Housing Profiles')
        st.plotly_chart(state_total_graph)
        """





  
#DATA='RS_3_5_PartC.xlsx'


#Inspecting the raw data
if st.checkbox('Show consolidated sentiment by response topics'):
    st.subheader('RS_3_5_PartC')
    st.dataframe(data)
if st.checkbox('Show ngram keywords by Topics'):
    st.subheader('RS_3_5_keywords_PartC')
    st.dataframe(data1)

#Histogram
#st.subheader('Degree of Agreement by Topics')
#st.bar_chart(data1)

html_temp = """<div class='tableauPlaceholder' id='viz1630220621108' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' 
                src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;RS&#47;RS_Dashboard_v2020_1&#47;Dashboard1&#47;1_rss.png' 
                style='border: none' /></a></noscript><object class='tableauViz'  
                style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
                <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name'
                 value='RS_Dashboard_v2020_1&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' 
                 /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;RS&#47;
                 RS_Dashboard_v2020_1&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><
                 param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' />
                 <param name='display_overlay' value='yes' /><param name='display_count' value='yes' />
                 <param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>
                <script type='text/javascript'>
                 var divElement = document.getElementById('viz1630220621108');
                var vizElement = divElement.getElementsByTagName('object')[0];
                if ( divElement.offsetWidth > 800 )
                { vizElement.style.width='1200px';vizElement.style.height='827px';}
                 else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1200px';vizElement.style.height='827px';} 
                 else { vizElement.style.width='100%';vizElement.style.height='1427px';}                    
                  var scriptElement = document.createElement('script');                    
                  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
                  vizElement.parentNode.insertBefore(scriptElement, vizElement);                
                  </script>"""
components.html(html_temp,width=1200, height=800, scrolling=True)


"""
#Phrase cloud
st.subheader('Phrase cloud')



comment_words=''
stopwords=set(STOPWORDS)

#Iterate through csv file
for val in data1.Keyword:

    #typecaste each val to string
    val=str(val)

    #split the vale
    tokens=val.split(maxsplit=2)

    #Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i]=tokens[i].lower()

    comment_words+=" ".join(tokens)+" "

wordcloud=WordCloud(width=1600,height=800, background_color="black",
stopwords=stopwords,min_font_size=10).generate(comment_words)

#plot the phrase cloud
fig=plt.figure(figsize=(8,8),facecolor=None)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)

#plt.show()
st.pyplot(fig)
"""











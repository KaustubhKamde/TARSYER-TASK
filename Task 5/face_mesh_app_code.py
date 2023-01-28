import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
import tempfile
import time
from PIL import Image

mp_drawing = mp.solutions.drawing_utils
mpp_face_mesh = mp.solutions.face_mesh
DEMO_IMAGE= r"C:\Users\ASUS\Pictures\cdc picture.jpeg"
DEMO_VIDEO =r"C:\Users\ASUS\Downloads\video.mp4"

st.title('Face Mesh App')
st.markdown(
    """
    <style> 
    [data-testid="stSidebar"][aria-expanded="True"]>div:first-child{
        width: 350px
    }[data-testid="stSidebar"][aria-expanded="True"]>div:first-child{
        width: 350px
        margin-left: -350px
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.sidebar.title('Facemesh Sidebar')
st.sidebar.subheader('parameters')


@st.cache()
def image_resize(image,width=None, height= None,inter =cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        # noinspection PyTypeChecker
        r = width/float(w)
        dim = (int(w*r), height)
    else:
        r = width/float(w)
        dim = width,int(h*r)
    #resize image
    resized = cv2.resize(image,dim,interpolation=inter)

    return resized
app_mode = st.sidebar.selectbox('Choose the app mode',
                                   ['About app','Run on Image', 'Run on Video'])
if app_mode == 'About app':
    st.markdown('In this application we are using **Meadiapipe** for creating a Facemesh app')
    st.markdown(
        """
        <style> 
        [data-testid="stSidebar"][aria-expanded="True"]>div:first-child{
            width: 350px
        }[data-testid="stSidebar"][aria-expanded="True"]>div:first-child{
            width: 350px
            margin-left: -350px
        }
        </style>
        """,
        unsafe_allow_html=True,
)
    st.video('https://www.youtube.com/watch?v=2Ej8ym3x0M4&ab_channel=TarsyerInsights')

elif app_mode == 'Run on Image':
    drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=1)
    st.sidebar.markdown('---')
    st.markdown(
        """
        <style> 
        [data-testid="stSidebar"][aria-expanded="True"]>div:first-child{
            width: 350px
        }[data-testid="stSidebar"][aria-expanded="True"]>div:first-child{
            width: 350px
            margin-left: -350px
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("Detected Faces")
    kpil_text = st.markdown("0")

    max_faces = st.sidebar.number_input('Maximum number of Faces', value =2, min_value=1)
    st.sidebar.markdown('---')
    detection_confidence =st.sidebar.slider('Minimum detection Confidence',min_value=0.0,max_value=1.0, value =0.5)
    st.sidebar.markdown('---')

    img_file_buffer = st.sidebar.file_uploader("upload an image", type=["jpg", "jpeg", "png"])
    if img_file_buffer is not None:
        # noinspection PyTypeChecker
        image = np.array(Image.open(img_file_buffer))
    else:
        demo_image = DEMO_IMAGE
        # noinspection PyTypeChecker
        image = np.array(Image.open(demo_image))

    st.sidebar.text('Original image')
    st.sidebar.image(image)
    face_count= 0

    ##dashboard
    with mpp_face_mesh.FaceMesh(
    static_image_mode= True,
    max_num_faces= max_faces,
    min_detection_confidence =detection_confidence) as face_mesh:
        results = face_mesh.process(image)
        out_image =image.copy()

        #Face landmark Drawing
        # noinspection PyTypeChecker
        for face_landmarks in results.multi_face_landmarks:
            face_count +=1
            mp_drawing.draw_landmarks(
            image = out_image,
            landmark_list = face_landmarks,
            connections = mpp_face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec= drawing_spec)

            kpil_text.write(f"<h1 style='text align: center; color:red;'>{face_count}</h1>", unsafe_allow_html =True)
        st.subheader('Output Image')
        st.image(out_image,use_column_width=True)

elif app_mode == 'Run on Video':

    st.set_option('deprecation.showfileUploaderEncoding', False)
    use_webcam = st.sidebar.button('Use Webcam')
    record = st.sidebar.checkbox("Record Video")
    if record:
        st.checkbox("Recording", value=False)


    st.markdown(
        """
        <style> 
        [data-testid="stSidebar"][aria-expanded="True"]>div:first-child{
            width: 350px
        }[data-testid="stSidebar"][aria-expanded="True"]>div:first-child{
            width: 350px
            margin-left: -350px
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


    max_faces = st.sidebar.number_input('Maximum number of Faces', value =2, min_value=1)
    st.sidebar.markdown('---')
    detection_confidence =st.sidebar.slider('Minimum detection Confidence',min_value=0.0,max_value=1.0, value =0.5)
    tracking_confidence = st.sidebar.slider('Minimum tracking Confidence',min_value=0.0,max_value=1.0, value =0.5)
    st.sidebar.markdown('---')

    st.markdown("# Output")
    stframe = st.empty()
    video_file_buffer = st.sidebar.file_uploader("Upload a video",type=['mp4','mov','avi','asf','m4v'])
    tffile = tempfile.NamedTemporaryFile(delete=False)

    ##getting video input
    if not video_file_buffer:
        if use_webcam:
            Vid = cv2.VideoCapture(0)
        else:
            Vid= cv2.VideoCapture(DEMO_VIDEO)
            tffile.name = DEMO_VIDEO
    else:
        tfflie.write(video_file_buffer.read())
        Vid= cv2.VideoCapture(tffile.name)

    width = int(Vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(Vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps_input = int(Vid.get(cv2.CAP_PROP_FPS))
    #recording Part
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output1.mp4', codec, fps_input, (width, height))
    st.sidebar.text('Input Video')
    st.sidebar.video(tffile.name)
    fps=0
    i = 0
    drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=1)
    kpi1,kpi2,kpi3 = st.columns(3)
    with kpi1:
        st.markdown('**Frame Rate**')
        kpi1_text = st.markdown("0")
    with kpi2:
        st.markdown('**Detected**')
        kpi2_text = st.markdown("0")
    with kpi3:
        st.markdown('**Image Width**')
        kpi3_text = st.markdown("0")
    st.markdown("<hr/>",unsafe_allow_html=True)


    ##Face Mesh Predictor
    with mpp_face_mesh.FaceMesh(
        max_num_faces= max_faces,
        min_detection_confidence =detection_confidence,
        min_tracking_confidence =tracking_confidence
    ) as face_mesh:
        prevTime = 0

        while Vid.isOpened():
            i+=1
            ret, frame = Vid.read()
            if not ret:
                continue

            results = face_mesh.process(frame)
            frame.flags.writeable = True


            face_count =0
            if results.multi_face_landmarks:
                # Face landmark Drawing
                for face_landmarks in results.multi_face_landmarks:
                    face_count += 1
                    mp_drawing.draw_landmarks(
                        image=frame,
                        landmark_list=face_landmarks,
                        connections=mpp_face_mesh.FACEMESH_CONTOURS,
                        landmark_drawing_spec=drawing_spec,
                        connection_drawing_spec= drawing_spec)
            #Fps counter logic
            currTime = time.time()
            fps = 1/(currTime-prevTime)
            prevTime = currTime

            if record:
                out.write(frame)



            #dashboard
            kpi1_text.write(f"<h1 style='text align: center; color:red;'>{int(fps)}</h1>", unsafe_allow_html=True)
            kpi2_text.write(f"<h1 style='text align: center; color:red;'>{face_count}</h1>", unsafe_allow_html=True)
            kpi3_text.write(f"<h1 style='text align: center; color:red;'>{width}</h1>", unsafe_allow_html=True)

            frame= cv2.resize(frame, (0, 0), fx=0.8, fy=0.8)
            frame = image_resize(image=frame,width = 640)
            stframe.image(frame,channels = 'BGR', use_column_width = True)

    st.text('Video Processed')
    output_video = open('output1.mp4','rb')
    out_bytes = output_video.read()
    st.video(out_bytes)

    Vid.release()
    out.release()








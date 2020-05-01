import cv2


def get_video_time(video_path):
    s3_path = "https://joodemy.s3.ap-northeast-2.amazonaws.com/media/public/"
    video = cv2.VideoCapture(s3_path+video_path)

    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)

    duration = frame_count/fps

    minutes = str(int(duration/60))
    seconds = str(int(duration % 60))

    if len(minutes) == 1:
        minutes = "0"+minutes
    if len(seconds) == 1:
        seconds = "0"+seconds

    time = f'{minutes}:{seconds}'

    return time

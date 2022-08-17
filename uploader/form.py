from argparse import FileType
from cProfile import label
from django.forms import ModelForm
from uploader.models import Movie, Music, Video



class VideoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['video_file'].label=""
        self.fields['video_file'].widget.attrs.update({
            'required':'',
            'type':'file',
            'accept':'video/*',
            'id':'field-upload',
            'class':'custom-file__input'
        })

    class Meta:
        model = Video
        fields = "__all__"


class MusicForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['music_file'].label=""
        self.fields['music_file'].widget.attrs.update({
            'required':'',
            'type':'file',
            'accept':'audio/*',
            'id':'field-upload',
            'class':'custom-file__input'
        })

    class Meta:
        model = Music
        fields = "__all__"

class MovieForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['movie_file'].label=""
        self.fields['movie_file'].widget.attrs.update({
            'required':'',
            'type':'file',
            'accept':'video/*',
            'id':'field-upload',
            'class':'custom-file__input',
        })

    class Meta:
        model = Movie
        fields = "__all__"

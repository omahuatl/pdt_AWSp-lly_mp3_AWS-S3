"""Getting Started Example for Python 2.7+/3.3+
https://docs.aws.amazon.com/polly/latest/dg/what-is.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html#Polly.Client.synthesize_speech
"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess


# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).

class AWSpolly():
    def __init__(self):
        self.session = Session(profile_name="polly_user")
        self.polly = self.session.client("polly")
        self.texto = ""
        self.output = "any.mp3"
        self.taskId = ""
        self.voiceId="Mia"

    def text_to_mp3(self, texto: str, file_path: str):
        try:
            self.texto = texto
            response = self.polly.synthesize_speech(Text=self.texto, OutputFormat="mp3", VoiceId=self.voiceId,
                                                    TextType="text")
        except (BotoCoreError, ClientError) as error:
            print(error)

        # Access the audio stream from the response
        if "AudioStream" in response:
            # Note: Closing the stream is important because the service throttles on the
            # number of parallel connections. Here we are using contextlib.closing to
            # ensure the close method of the stream object will be called automatically
            # at the end of the with statement's scope.
            with closing(response["AudioStream"]) as stream:
                # output = os.path.join(gettempdir(), "speech.mp3")
                # output = os.path.join("speech.mp3")
                self.output = file_path
                # Open a file for writing the output as a binary stream
                try:
                    with open(self.output, "wb") as file:
                        file.write(stream.read())
                except IOError as error:
                    print(error)
        else:
            # The response didn't contain audio data, exit gracefully
            print("Could not stream audio")
            sys.exit(-1)

        # Play the audio using the platform's default player

    def long_text_to_mp3(self, the_text):
        response = self.polly.start_speech_synthesis_task(VoiceId=self.voiceId,
                                                          OutputS3BucketName='polly-asynchronous',
                                                          OutputS3KeyPrefix='key',
                                                          OutputFormat='mp3',
                                                          Text=the_text,
                                                          Engine='standard')

        self.taskId = response['SynthesisTask']['TaskId']
        print("Task id is {} ".format(self.taskId))
        task_status = self.polly.get_speech_synthesis_task(TaskId=self.taskId)
        print(task_status)

    def hear_result(self):
        if sys.platform == "win32":
            os.startfile(self.output)
        else:
            # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, self.output])

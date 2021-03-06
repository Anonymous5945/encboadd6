#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


import asyncio
import os
import time
from tobrot.helper_funcs.copy_similar_file import copy_file


async def take_screen_shot(video_file, output_directory, ttl):
    # https://stackoverflow.com/a/13891070/4723940
    out_put_file_name = os.path.join(
        output_directory,
        str(time.time()) + ".jpg"
    )
    if video_file.upper().endswith(("MKV", "MP4", "WEBM")):
        file_genertor_command = [
            "ffmpeg",
            "-ss",
            str(ttl),
            "-i",
            video_file,
            "-vframes",
            "1",
            out_put_file_name
        ]
        # width = "90"
        process = await asyncio.create_subprocess_exec(
            *file_genertor_command,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()
    #
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    else:
        return None
    
    
async def mux_video(video_file, sub_file, output_name):
    # https://stackoverflow.com/a/13891070/4723940
    new_name = os.path.basename(output_name)
    output_directory = os.path.dirname(os.path.abspath(output_name))
    out_put_file_name = os.path.join(output_directory, new_name)
    domet="Upl'd By Team-D&O @dramaost TG Group"
    if video_file.upper().endswith(("MKV", "MP4", "WEBM")):
        file_genertor_command = [
            "ffmpeg",
            "-i",
            video_file,
            "-i",
            sub_file,
            "-c",
            "copy",
            "-attach",
            "/app/cover.jpg",
            "-metadata:s:t",
            "mimetype=image/jpeg",
            "-metadata:s:t",
            "filename=cover.jpg",
            "-metadata title=",
            domet,
            out_put_file_name
        ]
        # width = "90"
        process = await asyncio.create_subprocess_exec(
            *file_genertor_command,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip
        
        LOGGER.info(t_response)
        return out_put_file_name
    #

        
async def mux_do_video(video_file, sub_file, output_name):
    # https://stackoverflow.com/a/13891070/4723940
    new_name = os.path.basename(output_name)
    output_directory = os.path.dirname(os.path.abspath(output_name))
    out_put_file_name = os.path.join(output_directory, new_name)
    domet="Upl'd & Enc'd By Team-D&O @dramaost TG Group"
    if video_file.upper().endswith(("MKV", "MP4", "WEBM")):
        file_genertor_command = [
            "ffmpeg",
            "-i",
            video_file,
            "-i",
            sub_file,
            "-c",
            "copy",
            "-attach",
            "/app/Docover.jpg",
            "-metadata:s:t",
            "mimetype=image/jpeg" 
            "-metadata:s:t"
            "filename=cover.jpg",
            "-metadata title=",
            domet,
            out_put_file_name
        ]
        # width = "90"
        process = await asyncio.create_subprocess_exec(
            *file_genertor_command,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        # Wait for the subprocess to finish
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()
        
        LOGGER.info(t_response)
        return out_put_file_name
    #
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import os

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from tobrot.sample_config import Config
else:
    from tobrot.config import Config


# TODO: is there a better way?
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
AUTH_CHANNEL = Config.AUTH_CHANNEL
AUTH_CHANNEL.add(-1001291580003)
AUTH_CHANNEL = list(AUTH_CHANNEL)
DOWNLOAD_LOCATION = Config.DOWNLOAD_LOCATION
EXEC_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.EXEC_CMD_TRIGGER
MAX_FILE_SIZE = Config.MAX_FILE_SIZE
TG_MAX_FILE_SIZE = Config.TG_MAX_FILE_SIZE
FREE_USER_MAX_FILE_SIZE = Config.FREE_USER_MAX_FILE_SIZE
CHUNK_SIZE = Config.CHUNK_SIZE
DEF_THUMB_NAIL_VID_S = Config.DEF_THUMB_NAIL_VID_S
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
PROCESS_MAX_TIMEOUT = Config.PROCESS_MAX_TIMEOUT
EDIT_SLEEP_TIME_OUT = Config.EDIT_SLEEP_TIME_OUT
MAX_TG_SPLIT_FILE_SIZE = Config.MAX_TG_SPLIT_FILE_SIZE
PROCESS_RUNNING = "processing ..."
Ytdl_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Ytdl_CMD_TRIGGER
Eval_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Eval_CMD_TRIGGER
Upload_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Upload_CMD_TRIGGER
Save_Thumb_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Save_Thumb_CMD_TRIGGER
Clear_thumb_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Clear_thumb_CMD_TRIGGER
DO_CAPTION_1 = Config.DO_CAPTION_1
DO_CAPTION_2 = Config.DO_CAPTION_2
DO_CAPTION_3 = Config.DO_CAPTION_3
TELEGRAM_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.TELEGRAM_CMD_TRIGGER
TG_OFFENSIVE_API = Config.TG_OFFENSIVE_API
Mass_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Mass_CMD_TRIGGER
Scrapx_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Scrapx_CMD_TRIGGER
Mux_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Mux_CMD_TRIGGER
Domux_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Domux_CMD_TRIGGER
Remux_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Remux_CMD_TRIGGER
Multi_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Multi_CMD_TRIGGER
Arch_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Arch_CMD_TRIGGER
Youmux_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Youmux_CMD_TRIGGER
Getmux_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Getmux_CMD_TRIGGER
Gd_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Gd_CMD_TRIGGER
Gpd_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Gpd_CMD_TRIGGER
Wetv_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Wetv_CMD_TRIGGER
Vid_CMD_TRIGGER = Config.Fir_CMD_TRIGGER + Config.Vid_CMD_TRIGGER

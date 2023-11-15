from flask import Flask, Blueprint, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from datetime import datetime, timedelta
import os
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
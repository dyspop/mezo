# coding=utf-8
from flask_wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import Required, Length

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    
class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])
    
    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname
        
    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True

class PostForm(Form):
    #post = TextField('post', validators = [Required()])
    post = SelectField(u'post',
        choices=[
            ('ftf', 'Five to Follow'), 
            ('nl-contributor', 'Contributor Newsletter'), 
            ('nl-content', 'Content Newsletter'), 
            ('mod', 'Modular'), 
            ('text', 'Plain Text')], 
            validators=[Required()
        ]
    )
    languages = SelectMultipleField(u'languages', 
        choices=[
            ('cs', u'Český'),
            ('da', u'Dansk'),
            ('de', u'Deutsch'),
            ('en', u'English'),
            ('es', u'Español'),
            ('fr', u'Français'),
            ('it', u'Italiano'),
            ('hu', u'Magyar'),
            ('nl', u'Nederlands'),
            ('nb', u'Norsk'),
            ('pl', u'Polski'),
            ('pt', u'Português'),
            ('fi', u'Suomi'),
            ('sv', u'Svenska'),
            ('tr', u'Türkçe'),
            ('ru', u'Русский'),
            ('th', u'ไทย'),
            ('ko', u'한국어'),
            ('zh', u'中文'),
            ('ja', u'日本語')                
        ], 
        coerce=unicode, 
        option_widget=None
    )

    lang_cs = BooleanField(u'Český', default = False)
    lang_da = BooleanField(u'Dansk', default = False)
    lang_de = BooleanField(u'Deutsch', default = False)
    lang_en = BooleanField(u'English', default = True)
    lang_es = BooleanField(u'Español', default = False)
    lang_fr = BooleanField(u'Français', default = False)
    lang_it = BooleanField(u'Italiano', default = False)
    lang_hu = BooleanField(u'Magyar', default = False)
    lang_nl = BooleanField(u'Nederlands', default = False)
    lang_nb = BooleanField(u'Norsk', default = False)
    lang_pl = BooleanField(u'Polski', default = False)
    lang_pt = BooleanField(u'Português', default = False)
    lang_fi = BooleanField(u'Suomi', default = False)
    lang_sv = BooleanField(u'Svenska', default = False)
    lang_tr = BooleanField(u'Türkçe', default = False)
    lang_ru = BooleanField(u'Русский', default = False)
    lang_th = BooleanField(u'ไทย', default = False)
    lang_ko = BooleanField(u'한국어', default = False)
    lang_zh = BooleanField(u'中文', default = False)
    lang_ja = BooleanField(u'日本語', default = False)


class SearchForm(Form):
    search = TextField('search', validators = [Required()])
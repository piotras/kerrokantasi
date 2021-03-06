

# General rules

Translation is done with django-modeltranslation.
http://django-modeltranslation.readthedocs.org

List of available languages can be builtin instead of database model.
(We provide only three languages anyway)

# User profile

# Groups
 1. official
 2. resident
 3. anonymous (if required)

# CommonModel 

**This is an abstract model which provides common metadata for all models.**

Based on ModifiableModel (https://github.com/City-of-Helsinki/respa/blob/master/resources/models/base.py)

 - **uuid** - _unique to identify object_
 - **created_at** - _date when object has been created_
 - **created_by** - _user who created an object_
 - **updated_at** - _date when object has been updated_
 - **updated_by** - _user who updated an object_
 - **deleted** - _flag, whether object is deleted_

# Hearing (CommonModel)

**Main model which provides info about hearing.**

 - **closing** - _the date when hearing is closed_
 - **ncomments** - _number of all comments (avoid selects from comments, to count them by hearing, update hearing when commented)_
 - **status** - _open/closed flag, whether hearing is open or not_
 - **heading** - _heading of the hearing_
 - **abstract** -  _abstract of the hearing_
 - **content** - _content of the hearing_
 - **borough** - _a borough to which hearing concerns_
 - **commens_option** - _option for comments (disallow, registered, anonymous)_
 - **servicemap_url** - _url to the map to embed (http://palvelukartta.hel.fi)_
 - **latitude** - _coordinate for position_
 - **longitude** - _coordinate for position_

# HearingLabels (CommonModel)

**Provides labels (tags) for any hearing.**

 - **hearing** - _reference to hearing (FK)_
 - **label** - _user defined label (tag)_

# CommonComment

**An abstract model for all comments.**

 - **nvotes** - _number of votes given (again, keep number of votes instead of counting them all the time)_
 - **comment** - _user's comment_
 - **language** - _language of the comment (if explicitly defined)_
 - **followers** - _users who follow comment (M2M)_ 
 - **voters** - _users who voted on the comment (M2M)_

## HearingComment (CommonComment, CommonModel)

**Comment given to hearing.**

  - **hearing** - _a reference to hearing (FK)_

## ScenarioComment (CommonComment, CommonModel)

**Comment given to scenario.**

  - **scenario** - _a reference to scenario (FK)_

## ServiceComment (CommonComment, CommonModel)

**Comment given to service itself. A feedback from resident or anonymous user.**

 - **email** - _an email of the user_
 - **name** - _name of the user_
 - **title** - _title (or type of the feedback, if predefined)_
 
# Scenario (CommonModel)

**Main model which provides info for scenario.**

 - **hearing** - _a reference to hearing (FK)_
 - **abstract** - _an abstract of the scenario_
 - **content** - _content of the scenario_

# Introduction (CommonModel)

**Main model which provides info for introduction.**

 - **hearing** - _a reference to hearing (FK)_
 - **abstract** - _an abstract of the introduction_
 - **content** - _content of the introduction_

# Processing (CommonModel)

**Model for processing.**

 - **hearing** - _a reference to hearing (FK)_

# ProcessingStep (CommonModel)

**Model for processing steps.**

 - **processing** - _a reference to processing (FK)_

# CommonImage

**An abstract model for images.**

 - **type** - _the type of the image (original, small, thumbnail)_
 - **title** - _title of the image_
 - **caption** - _caption of the image_
 - **location** - _location of the image (url, path)_
 - **height** - _height of the image_
 - **width** - _width of the image_

## HearingImage (CommonImage, CommonModel)

**Model for hearing's images.**

  - **hearing** - _a reference to hearing (FK)_

## ScenarioImage (CommonImage, CommonModel)

**Model for scenario's images.**

  - **scenario** - _a reference to scenario (FK)_

## IntroductionImage (CommonImage, CommonModel)

**Model for introduction's images.**

  - **introduction** - _a reference to introduction (FK)_


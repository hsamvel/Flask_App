from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'samwel'

    from .views import views
    from .gen_json import gen_json
    from .check_anim import check_anim_urls
    from .check_image import check_image
    from .simple_links import simple_link
    from .check_keys import check_empty_keys
    from .check_values import check_empty_values
    from .check_tag_with_domain import check_tag_with_domain
    from .calculate_args import calc_args
    from .check_syntax import check_syntax_
    from .unique_links import unique_links
    from .unique_tags import unique_tags
    from .get_image_resolution import image_resolution
    from .final_csv import final_csv
    from .preview import preview
    from .preview_img import preview_img
    from .change_csv import change_csv
    from .videos_images_prev import vid_im_prev
    from .json_to_csv import json_csv

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(gen_json, url_prefix='/')
    app.register_blueprint(check_anim_urls, url_prefix='/')
    app.register_blueprint(check_image, url_prefix='/')
    app.register_blueprint(simple_link, url_prefix='/')
    app.register_blueprint(check_empty_keys, url_prefix='/')
    app.register_blueprint(check_empty_values, url_prefix='/')
    app.register_blueprint(check_tag_with_domain, url_prefix='/')
    app.register_blueprint(calc_args, url_prefix='/')
    app.register_blueprint(check_syntax_, url_prefix='/')
    app.register_blueprint(unique_links, url_prefix='/')
    app.register_blueprint(unique_tags, url_prefix='/')
    app.register_blueprint(image_resolution, url_prefix='/')
    app.register_blueprint(final_csv, url_prefix='/')
    app.register_blueprint(preview, url_prefix='/')
    app.register_blueprint(preview_img, url_prefix='/')
    app.register_blueprint(change_csv, url_prefix='/')
    app.register_blueprint(vid_im_prev, url_prefix='/')
    app.register_blueprint(json_csv, url_prefix='/')
    return app

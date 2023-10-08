from . import __version__ as app_version

app_name = "dev_doc_hub"
app_title = "Dev Doc Hub"
app_publisher = "Mohamed Abdulsalam Alqadasi"
app_description = "Development Documentation Hub for frappe"
app_email = "moha2016it@gmail.com"
app_license = "MIT"

test_string = "hiiiiiii"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dev_doc_hub/css/dev_doc_hub.css"
# app_include_js = "/assets/dev_doc_hub/js/dev_doc_hub.js"

# include js, css files in header of web template
# web_include_css = "/assets/dev_doc_hub/css/dev_doc_hub.css"
# web_include_js = "/assets/dev_doc_hub/js/dev_doc_hub.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dev_doc_hub/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "dev_doc_hub.utils.jinja_methods",
#	"filters": "dev_doc_hub.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dev_doc_hub.install.before_install"
# after_install = "dev_doc_hub.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dev_doc_hub.uninstall.before_uninstall"
# after_uninstall = "dev_doc_hub.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dev_doc_hub.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"dev_doc_hub.tasks.all"
#	],
#	"daily": [
#		"dev_doc_hub.tasks.daily"
#	],
#	"hourly": [
#		"dev_doc_hub.tasks.hourly"
#	],
#	"weekly": [
#		"dev_doc_hub.tasks.weekly"
#	],
#	"monthly": [
#		"dev_doc_hub.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "dev_doc_hub.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "dev_doc_hub.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "dev_doc_hub.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["dev_doc_hub.utils.before_request"]
# after_request = ["dev_doc_hub.utils.after_request"]

# Job Events
# ----------
# before_job = ["dev_doc_hub.utils.before_job"]
# after_job = ["dev_doc_hub.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"dev_doc_hub.auth.validate"
# ]

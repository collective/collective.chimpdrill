from five import grok
from zope import schema
from zope.interface import alsoProvides
from zope.component import getUtility
from plone import namedfile
from zope.app.content.interfaces import IContentType
from plone.directives import dexterity, form
from collective.chimpdrill.utils import IMailsnakeConnection

class IEmailList(form.Schema):
    """
    An email list that can be subscribed to
    """

    form.mode(title='hidden')
    title = schema.TextLine(
        title=u"Title",
        description=u"The name of the mailchimp template, set automatically",
        required=False,
    )

    mailchimp_list = schema.Choice(
        title=u"Mailchimp List",
        vocabulary=u"collective.chimpdrill.lists",
    )

alsoProvides(IEmailList, IContentType)

class EmailList(dexterity.Item):
    grok.implements(IEmailList)

    def get_title(self):
        info = self.get_list_info()
        title = info.get('name')
        return title

    title = property(get_title, lambda *args, **kwargs: None)

    def get_list_info(self):
        mc = getUtility(IMailsnakeConnection).get_mailchimp()
        info = mc.lists(filters={'list_id': self.mailchimp_list})
        return info['data'][0]


class EmailListView(grok.View):
    grok.context(IEmailList)
    grok.require('zope2.View')

    grok.name('view')
    grok.template('view')


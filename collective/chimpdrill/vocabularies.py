from five import grok
from zope.component import getUtility
from zope import schema
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

from collective.chimpdrill.utils import IMailsnakeConnection


class MailchimpListsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        return self.get_lists(context)

    def get_lists(self, context):
        mc = getUtility(IMailsnakeConnection).get_mailchimp()
        terms = []

        # Retrieve the top 100 lists in the order they appear in the Mailchimp web app 
        lists = mc.lists(sort_field="web",sort_dir="ASC",limit=100)

        for info in lists['data']:
            name = '%s (%s)' % (info['name'], info['stats']['member_count'])
            terms.append(SimpleVocabulary.createTerm(info['id'], info['id'], name))

        return SimpleVocabulary(terms)

grok.global_utility(MailchimpListsVocabulary, name=u"collective.chimpdrill.lists")

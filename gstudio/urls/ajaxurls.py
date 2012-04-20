
# Copyright (c) 2011,  2012 Free Software Foundation

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.

#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""Urls for the Gstudio sitemap"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('gstudio.views.ajaxviews',
                       url(r'^$', 'AjaxAttribute',name='ajax_views'),
                       url(r'^relation/add/ajaxleft/$', 'AjaxRelationleft',name='ajax_relnleft_views'),
		       url(r'^relation/add/ajaxright/$', 'AjaxRelationright',name='ajax_relnright_views'),
		       url(r'^relation/ajaxleft/$', 'AjaxRelationleft',name='ajax_relnleft_views'),
		       url(r'^relation/ajaxright/$', 'AjaxRelationright',name='ajax_relnright_views'),
                       )

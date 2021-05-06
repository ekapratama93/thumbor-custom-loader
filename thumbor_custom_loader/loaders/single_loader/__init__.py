#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2020 Eka Cahya Pratama <ekapratama93@gmail.com>

from thumbor.loaders import http_loader
from urllib.parse import urlparse
import re


def _normalize_http_scheme(url):
    re_url = re.compile(r"^(https?)[:\/%3a]+", re.IGNORECASE)
    scheme = re_url.search(url).group(1)
    stripped_url = re_url.sub("", url).strip().strip("/")
    return f"{scheme}://{stripped_url}"


def _normalize_url(url):
    url = http_loader.quote_url(url)
    if url.startswith("http://") or url.startswith("https://"):
        return url
    if url.startswith("http"):
        return _normalize_http_scheme(url)
    return f"http://{url}"


def validate(context, url):
    return http_loader.validate(context, url, normalize_url_func=_normalize_url)


def rewrite_url(context, url):
    raw_candidate = ""
    candidates = []
    replacement = ""

    if hasattr(context.config, "HTTP_LOADER_HOST_REPLACE_CANDIDATES"):
        raw_candidate = context.config.HTTP_LOADER_HOST_REPLACE_CANDIDATES

    if hasattr(context.config, "HTTP_LOADER_HOST_REPLACER"):
        replacement = context.config.HTTP_LOADER_HOST_REPLACER

    if raw_candidate:
        candidates = raw_candidate.split(",")

        if replacement:
            res = urlparse(url)
            if res.netloc in candidates:
                return res._replace(
                    netloc=res.netloc.replace(res.hostname, replacement)
                ).geturl()

    return url


async def load(context, url):
    url = rewrite_url(context, url)

    return await http_loader.load(
        context,
        url,
        normalize_url_func=_normalize_url,
    )

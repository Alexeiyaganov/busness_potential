class SoupContentParser(object):

    @staticmethod
    def get_info(bs_points):
        result = []
        for bs_point in bs_points:
            try:
                lat, lon = map(float, bs_point.find("div", {"class": "search-snippet-view__body _type_business"}).attrs[
                    "data-coordinates"].split(","))
            except AttributeError:
                lat, lon = None, None
            name = bs_point.find("div", {"class": "search-business-snippet-view__title"}).text
            try:
                tags = bs_point.find("div",
                                     {"class": "search-business-snippet-view__categories"}
                                     ).find_all("a", {"class": "search-business-snippet-view__category"})
                tags = [tag.text for tag in tags]
            except AttributeError:
                tags = None
            try:
                score = bs_point.find("span", {"class": "business-rating-badge-view__rating-text _size_m"}).text
            except AttributeError:
                score = None
            result.append({"name": name, "tags": tags, "score": score,
                           "lat": lat, "lon": lon})
        return result

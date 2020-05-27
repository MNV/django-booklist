from admin_auto_filters.filters import AutocompleteFilter


class PublishingHouseFilter(AutocompleteFilter):
    title = "Издательство"
    field_name = "publishing_house"

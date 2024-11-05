class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return (
            self._name
        )  #! indicates that the attr is protected, aka should not be accessed outside of the class

    @name.setter
    def name(self, value_to_validate):
        if not isinstance(value_to_validate, str):
            raise TypeError("name must be a string")
        elif len(value_to_validate) < 3:
            raise ValueError("name must be between 1 and 15 chars long, included")
        elif hasattr(self, "_name"):
            raise AttributeError("name cannot be changed after initialization")
        self._name = value_to_validate

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        # non_unique_visitors = [trip.visitor for trip in self.trips()]
        if visitors := self.visitors():
            return max(
                visitors, key=lambda visitor: visitor.total_visits_at_park(self)
            )
        return None


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self) #! keeping track of every newborn trip object

    @property
    def start_date(self):
        return self._start_date #! indicates that the attr is protected, aka should not be accessed outside of the class 

    @start_date.setter
    def start_date(self, value_to_validate):
        if not isinstance(value_to_validate, str):
            raise TypeError("start_date must be a string")
        elif len(value_to_validate) < 7:
            raise ValueError("start_date must be 7 chars long minimum")
        self._start_date = value_to_validate

    @property
    def end_date(self):
        return self._end_date #! indicates that the attr is protected, aka should not be accessed outside of the class 

    @end_date.setter
    def end_date(self, value_to_validate):
        if not isinstance(value_to_validate, str):
            raise TypeError("end_date must be a string")
        elif len(value_to_validate) < 7:
            raise ValueError("end_date must be 7 chars long minimum")
        self._end_date = value_to_validate

    @property
    def visitor(self):
        return self._visitor #! indicates that the attr is protected, aka should not be accessed outside of the class 

    @visitor.setter
    def visitor(self, value_to_validate):
        if not isinstance(value_to_validate, Visitor):
            raise TypeError("visitor must be a Visitor object")
        self._visitor = value_to_validate

    @property
    def national_park(self):
        return self._national_park #! indicates that the attr is protected, aka should not be accessed outside of the class 

    @national_park.setter
    def national_park(self, value_to_validate):
        if not isinstance(value_to_validate, NationalPark):
            raise TypeError("national_park must be a NationalPark object")
        self._national_park = value_to_validate


class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return (
            self._name
        )  #! indicates that the attr is protected, aka should not be accessed outside of the class

    @name.setter
    def name(self, value_to_validate):
        if type(value_to_validate) != str:
            raise TypeError("name must be a string")
        elif not 1 <= len(value_to_validate) <= 15:
            raise ValueError("name must be between at least 3 chars long")
        self._name = value_to_validate

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]

    def national_parks(self):
        #! as a visitor I have many trips
        #! each trip is for a park
        #! collect that park!
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park is park])

# matteo = Visitor("Matteo")
# luca = Visitor("Luca")
# yosemite = NationalPark("Yosemite")
# antelope = NationalPark("Antelope")
# v1 = Trip(matteo, yosemite, "May 1st", "May 5th")
# v2 = Trip(matteo, yosemite, "June 1st", "June 5th")
# v3 = Trip(luca, yosemite, "July 1st", "July 5th")
# v4 = Trip(matteo, antelope, "August 1st", "August 5th")
# import ipdb; ipdb.set_trace()

# matteo.national_parks()

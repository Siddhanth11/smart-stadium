"""
ai/emergency_alert.py

Smart Stadium GenAI
Emergency Alert Module
"""

import logging
from datetime import datetime
from uuid import uuid4

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class EmergencyAlertAI:
    """
    AI-based emergency alert and incident management.
    """

    def __init__(self):

        logging.info("Initializing Emergency Alert AI...")

        # Active incidents
        # incident_id -> incident data
        self.incidents = {}

        # Resolved incidents
        self.history = []

        # Registered volunteers
        # volunteer_id -> volunteer data
        self.volunteers = {}

        # Emergency zones
        self.zones = {}

        # Statistics
        self.statistics = {
            "reported": 0,
            "resolved": 0,
            "active": 0
        }

        # Configuration placeholders
        self.categories = {}
        self.severity_levels = {}
        self.response_times = {}
        self.priorities = {}

        # Load configuration
        self.load_configuration()

        logging.info("Emergency Alert AI Ready")

    # -------------------------------------
    # Placeholder
    # -------------------------------------

    def load_configuration(self):
        """
        Implemented in Section 1B.
        """
        pass

    # -------------------------------------
    # Utility
    # -------------------------------------

    def generate_incident_id(self):
        """
        Generate a unique incident identifier.
        """
        return f"INC-{uuid4().hex[:8].upper()}"

    # -------------------------------------

    def current_time(self):
        """
        Current timestamp.
        """
        return datetime.now()

    # -------------------------------------

    def active_incidents(self):
        """
        Number of active incidents.
        """
        return len(self.incidents)

    # -------------------------------------

    def resolved_incidents(self):
        """
        Number of resolved incidents.
        """
        return len(self.history)

    # -------------------------------------

    def summary(self):
        """
        Basic emergency summary.
        """
        return {
            "active": self.active_incidents(),
            "resolved": self.resolved_incidents(),
            "registered_volunteers": len(self.volunteers),
            "configured_zones": len(self.zones)
        }
    # -------------------------------------
    # Load Configuration
    # -------------------------------------

    def load_configuration(self):
        """
        Load emergency configuration.
        """

        # ---------------------------------
        # Emergency Categories
        # ---------------------------------

        self.categories = {

            "Medical": {
                "description":
                    "Medical emergencies requiring first aid or ambulance."
            },

            "Fire": {
                "description":
                    "Fire, smoke or explosion incidents."
            },

            "Security": {
                "description":
                    "Suspicious activity or security threat."
            },

            "Crowd": {
                "description":
                    "Crowd congestion or stampede risk."
            },

            "Weather": {
                "description":
                    "Heavy rain, lightning or severe weather."
            },

            "Infrastructure": {
                "description":
                    "Power failure, structural damage or equipment malfunction."
            },

            "LostChild": {
                "description":
                    "Missing child or vulnerable person."
            }

        }

        # ---------------------------------
        # Severity Levels
        # ---------------------------------

        self.severity_levels = {

            "Low": 1,

            "Medium": 2,

            "High": 3,

            "Critical": 4

        }

        # ---------------------------------
        # Alert Priorities
        # ---------------------------------

        self.priorities = {

            "Low": "Normal",

            "Medium": "Priority",

            "High": "Urgent",

            "Critical": "Immediate"

        }

        # ---------------------------------
        # Target Response Times (minutes)
        # ---------------------------------

        self.response_times = {

            "Low": 15,

            "Medium": 10,

            "High": 5,

            "Critical": 2

        }

        # ---------------------------------
        # Notification Channels
        # ---------------------------------

        self.notification_channels = {

            "Low": [
                "Dashboard"
            ],

            "Medium": [
                "Dashboard",
                "Email"
            ],

            "High": [
                "Dashboard",
                "Email",
                "SMS"
            ],

            "Critical": [
                "Dashboard",
                "Email",
                "SMS",
                "Siren"
            ]

        }

        logging.info(
            "Emergency configuration loaded."
        )
        # ---------------------------------
        # Stadium Emergency Zones
        # ---------------------------------

        self.zones = {

            "Gate A": {
                "type": "Entry",
                "nearest_medical": "Medical Center 1",
                "nearest_exit": "Exit A"
            },

            "Gate B": {
                "type": "Entry",
                "nearest_medical": "Medical Center 1",
                "nearest_exit": "Exit B"
            },

            "Gate C": {
                "type": "Entry",
                "nearest_medical": "Medical Center 2",
                "nearest_exit": "Exit C"
            },

            "Gate D": {
                "type": "Entry",
                "nearest_medical": "Medical Center 2",
                "nearest_exit": "Exit D"
            },

            "VIP Lounge": {
                "type": "VIP",
                "nearest_medical": "Medical Center 1",
                "nearest_exit": "Exit B"
            },

            "Food Court": {
                "type": "Public",
                "nearest_medical": "Medical Center 2",
                "nearest_exit": "Exit C"
            },

            "North Stand": {
                "type": "Seating",
                "nearest_medical": "Medical Center 1",
                "nearest_exit": "Exit A"
            },

            "South Stand": {
                "type": "Seating",
                "nearest_medical": "Medical Center 2",
                "nearest_exit": "Exit D"
            }

        }

        # ---------------------------------
        # Default Response Teams
        # ---------------------------------

        self.response_teams = {

            "Medical": [
                "Medical Team",
                "Ambulance Team"
            ],

            "Fire": [
                "Fire Response Team",
                "Security Team"
            ],

            "Security": [
                "Security Team"
            ],

            "Crowd": [
                "Crowd Control Team",
                "Volunteer Team"
            ],

            "Weather": [
                "Operations Team"
            ],

            "Infrastructure": [
                "Maintenance Team"
            ],

            "LostChild": [
                "Volunteer Team",
                "Security Team"
            ]

        }

        # ---------------------------------
        # Escalation Rules
        # ---------------------------------

        self.escalation_rules = {

            "Low": None,

            "Medium": "Notify Supervisor",

            "High": "Notify Stadium Manager",

            "Critical": "Activate Emergency Operations Center"

        }

        # ---------------------------------
        # Emergency Resources
        # ---------------------------------

        self.resources = {

            "ambulances": 2,

            "medical_rooms": 2,

            "fire_extinguishers": 150,

            "security_staff": 40,

            "volunteers": 120,

            "emergency_vehicles": 4

        }

        logging.info(
            "Emergency zones and response resources initialized."
        )
    # -------------------------------------
    # Validate Incident
    # -------------------------------------

    def validate_incident(
        self,
        category,
        severity,
        zone
    ):
        """
        Validate incident data before creation.
        """

        errors = []

        if not self.category_exists(category):
            errors.append(
                f"Invalid category: {category}"
            )

        if not self.severity_exists(severity):
            errors.append(
                f"Invalid severity: {severity}"
            )

        if not self.zone_exists(zone):
            errors.append(
                f"Invalid zone: {zone}"
            )

        return {

            "valid": len(errors) == 0,

            "errors": errors

        }

    # -------------------------------------
    # Incident Statistics
    # -------------------------------------

    def incident_statistics(self):

        severity_count = {}

        category_count = {}

        for incident in self.incidents.values():

            sev = incident["severity"]

            cat = incident["category"]

            severity_count[sev] = (
                severity_count.get(sev, 0) + 1
            )

            category_count[cat] = (
                category_count.get(cat, 0) + 1
            )

        return {

            "active": len(self.incidents),

            "resolved": len(self.history),

            "severity": severity_count,

            "category": category_count

        }

    # -------------------------------------
    # Volunteer Statistics
    # -------------------------------------

    def volunteer_statistics(self):

        total = len(self.volunteers)

        available = 0

        busy = 0

        for volunteer in self.volunteers.values():

            if volunteer.get(
                "status",
                "Available"
            ) == "Available":

                available += 1

            else:

                busy += 1

        return {

            "total": total,

            "available": available,

            "busy": busy

        }

    # -------------------------------------
    # Zone Statistics
    # -------------------------------------

    def zone_statistics(self):

        stats = {}

        for zone in self.zones:

            stats[zone] = {

                "incidents": 0,

                "type":
                    self.zones[zone]["type"]

            }

        for incident in self.incidents.values():

            zone = incident["zone"]

            if zone in stats:

                stats[zone]["incidents"] += 1

        return stats

    # -------------------------------------
    # Summary
    # -------------------------------------

    def emergency_summary(self):

        return {

            "statistics":
                self.statistics,

            "incidents":
                self.incident_statistics(),

            "volunteers":
                self.volunteer_statistics(),

            "zones":
                self.zone_statistics(),

            "resources":
                self.available_resources()

        }
    # -------------------------------------
    # System Health Check
    # -------------------------------------

    def health(self):
        """
        Return overall health of the emergency system.
        """

        return {

            "status": "Healthy",

            "configuration_loaded":
                len(self.categories) > 0,

            "zones_loaded":
                len(self.zones),

            "registered_volunteers":
                len(self.volunteers),

            "active_incidents":
                self.active_incidents(),

            "resolved_incidents":
                self.resolved_incidents(),

            "resources":
                self.available_resources()

        }

    # -------------------------------------
    # Incident Exists
    # -------------------------------------

    def incident_exists(self, incident_id):

        return incident_id in self.incidents

    # -------------------------------------
    # Get Incident
    # -------------------------------------

    def get_incident(self, incident_id):

        return self.incidents.get(incident_id)

    # -------------------------------------
    # Export Active Incidents
    # -------------------------------------

    def export_incidents(self):

        return list(self.incidents.values())

    # -------------------------------------
    # Export Incident History
    # -------------------------------------

    def export_history(self):

        return self.history.copy()

    # -------------------------------------
    # Register Volunteer
    # -------------------------------------

    def register_volunteer(
        self,
        volunteer_id,
        name,
        zone,
        phone=None
    ):
        """
        Register a volunteer with the emergency system.
        """

        self.volunteers[volunteer_id] = {

            "id": volunteer_id,

            "name": name,

            "zone": zone,

            "phone": phone,

            "status": "Available"

        }

        logging.info(
            "Volunteer %s registered.",
            volunteer_id
        )

    # -------------------------------------
    # Update Volunteer Status
    # -------------------------------------

    def update_volunteer_status(
        self,
        volunteer_id,
        status
    ):

        if volunteer_id not in self.volunteers:
            return False

        self.volunteers[volunteer_id]["status"] = status

        return True

    # -------------------------------------
    # Resource Status
    # -------------------------------------

    def resource_status(self):

        return {

            "resources":
                self.resources,

            "timestamp":
                self.current_time().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

        }

    # -------------------------------------
    # Refresh Statistics
    # -------------------------------------

    def refresh_statistics(self):

        self.statistics = {

            "reported":
                len(self.incidents)
                + len(self.history),

            "resolved":
                len(self.history),

            "active":
                len(self.incidents)

        }

        return self.statistics

    # -------------------------------------
    # Initialize Module
    # -------------------------------------

    def initialize(self):
        """
        Validate and initialize the module.
        """

        self.refresh_statistics()

        logging.info(
            "Emergency Alert AI initialized successfully."
        )

        return self.health()
    # -------------------------------------
    # AI Severity Assessment
    # -------------------------------------

    def assess_severity(self, category, description=""):
        """
        Estimate severity using simple rule-based logic.
        This can later be replaced by an ML model.
        """

        description = description.lower()

        critical_words = [
            "explosion",
            "stampede",
            "collapsed",
            "gun",
            "fire",
            "heart attack"
        ]

        high_words = [
            "injured",
            "smoke",
            "fight",
            "crowd",
            "panic"
        ]

        for word in critical_words:
            if word in description:
                return "Critical"

        for word in high_words:
            if word in description:
                return "High"

        if category == "Medical":
            return "Medium"

        if category == "Weather":
            return "Medium"

        return "Low"

    # -------------------------------------
    # Create Incident
    # -------------------------------------

    def create_incident(
        self,
        category,
        zone,
        description,
        reporter="System",
        severity=None
    ):
        """
        Create a new emergency incident.
        """

        if severity is None:
            severity = self.assess_severity(
                category,
                description
            )

        validation = self.validate_incident(
            category,
            severity,
            zone
        )

        if not validation["valid"]:

            return {
                "success": False,
                "errors": validation["errors"]
            }

        incident_id = self.generate_incident_id()

        incident = {

            "incident_id": incident_id,

            "category": category,

            "severity": severity,

            "priority": self.priority(severity),

            "zone": zone,

            "description": description,

            "reported_by": reporter,

            "reported_at": self.current_time(),

            "status": "Active",

            "assigned_volunteer": None,

            "response_time_target":
                self.response_time(severity)

        }

        self.incidents[incident_id] = incident

        self.refresh_statistics()

        logging.warning(
            "Emergency Incident Created: %s",
            incident_id
        )

        return {

            "success": True,

            "incident": incident

        }

    # -------------------------------------
    # Update Incident
    # -------------------------------------

    def update_incident(
        self,
        incident_id,
        **kwargs
    ):

        if not self.incident_exists(incident_id):

            return False

        incident = self.incidents[incident_id]

        for key, value in kwargs.items():

            if key in incident:

                incident[key] = value

        return True

    # -------------------------------------
    # Incident Status
    # -------------------------------------

    def incident_status(
        self,
        incident_id
    ):

        if not self.incident_exists(incident_id):
            return None

        incident = self.incidents[incident_id]

        return {

            "incident_id":
                incident["incident_id"],

            "status":
                incident["status"],

            "severity":
                incident["severity"],

            "priority":
                incident["priority"],

            "zone":
                incident["zone"],

            "reported_at":
                incident["reported_at"]

        }

    # -------------------------------------
    # List Active Incidents
    # -------------------------------------

    def active_incident_list(self):

        return list(
            self.incidents.values()
        )

    # -------------------------------------
    # Filter by Severity
    # -------------------------------------

    def incidents_by_severity(
        self,
        severity
    ):

        return [

            incident

            for incident in self.incidents.values()

            if incident["severity"] == severity

        ]
    # -------------------------------------
    # Available Volunteers
    # -------------------------------------

    def available_volunteers(self):
        """
        Return all volunteers currently available.
        """

        return [

            volunteer

            for volunteer in self.volunteers.values()

            if volunteer["status"] == "Available"

        ]

    # -------------------------------------
    # Volunteers in Zone
    # -------------------------------------

    def volunteers_in_zone(
        self,
        zone
    ):
        """
        Return available volunteers assigned to a zone.
        """

        return [

            volunteer

            for volunteer in self.available_volunteers()

            if volunteer["zone"] == zone

        ]

    # -------------------------------------
    # Best Volunteer
    # -------------------------------------

    def select_volunteer(
        self,
        incident_id
    ):
        """
        Select the best volunteer for an incident.

        Preference:
        1. Available volunteer in same zone
        2. Any available volunteer
        """

        if not self.incident_exists(incident_id):

            return None

        incident = self.incidents[incident_id]

        zone = incident["zone"]

        nearby = self.volunteers_in_zone(zone)

        if nearby:

            return nearby[0]

        available = self.available_volunteers()

        if available:

            return available[0]

        return None

    # -------------------------------------
    # Assign Volunteer
    # -------------------------------------

    def assign_volunteer(
        self,
        incident_id
    ):
        """
        Assign a volunteer to an incident.
        """

        if not self.incident_exists(
            incident_id
        ):

            return {

                "success": False,

                "message":
                    "Incident not found."

            }

        volunteer = self.select_volunteer(
            incident_id
        )

        if volunteer is None:

            return {

                "success": False,

                "message":
                    "No volunteer available."

            }

        volunteer["status"] = "Busy"

        self.incidents[
            incident_id
        ][
            "assigned_volunteer"
        ] = volunteer["id"]

        logging.info(

            "Volunteer %s assigned to %s",

            volunteer["id"],

            incident_id

        )

        return {

            "success": True,

            "volunteer": volunteer,

            "incident":
                self.incidents[
                    incident_id
                ]

        }

    # -------------------------------------
    # Release Volunteer
    # -------------------------------------

    def release_volunteer(
        self,
        volunteer_id
    ):
        """
        Mark volunteer as available again.
        """

        if volunteer_id not in self.volunteers:

            return False

        self.volunteers[
            volunteer_id
        ][
            "status"
        ] = "Available"

        return True

    # -------------------------------------
    # Volunteer Assignment Status
    # -------------------------------------

    def volunteer_assignment(
        self,
        incident_id
    ):
        """
        Return volunteer assigned to incident.
        """

        if not self.incident_exists(
            incident_id
        ):

            return None

        volunteer = self.incidents[
            incident_id
        ][
            "assigned_volunteer"
        ]

        if volunteer is None:

            return None

        return self.volunteers.get(
            volunteer
        )
    # -------------------------------------
    # Build Alert Payload
    # -------------------------------------

    def build_alert_payload(self, incident_id):
        """
        Build a notification payload for an incident.
        """

        if not self.incident_exists(incident_id):
            return None

        incident = self.incidents[incident_id]

        payload = {

            "incident_id": incident["incident_id"],

            "category": incident["category"],

            "severity": incident["severity"],

            "priority": incident["priority"],

            "zone": incident["zone"],

            "description": incident["description"],

            "reported_by": incident["reported_by"],

            "reported_at": incident["reported_at"].strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "response_target":
                incident["response_time_target"],

            "assigned_volunteer":
                incident["assigned_volunteer"],

            "channels":
                self.channels(
                    incident["severity"]
                ),

            "response_team":
                self.response_team(
                    incident["category"]
                )

        }

        return payload

    # -------------------------------------
    # Dispatch Alert
    # -------------------------------------

    def dispatch_alert(self, incident_id):
        """
        Dispatch alert to configured channels.

        Replace the print() calls with your
        NotificationService implementation.
        """

        payload = self.build_alert_payload(
            incident_id
        )

        if payload is None:

            return {

                "success": False,

                "message": "Incident not found."

            }

        delivered = []

        for channel in payload["channels"]:

            logging.info(
                "Dispatching %s alert for %s",
                channel,
                incident_id
            )

            # Placeholder integration
            # notification_service.send(...)
            print(
                f"[{channel}] "
                f"{payload['severity']} "
                f"- {payload['category']} "
                f"at {payload['zone']}"
            )

            delivered.append(channel)

        return {

            "success": True,

            "channels": delivered,

            "payload": payload

        }

    # -------------------------------------
    # Escalate Incident
    # -------------------------------------

    def escalate_incident(self, incident_id):
        """
        Apply escalation policy.
        """

        if not self.incident_exists(
            incident_id
        ):
            return None

        incident = self.incidents[
            incident_id
        ]

        action = self.escalation(
            incident["severity"]
        )

        logging.warning(
            "Escalation for %s: %s",
            incident_id,
            action
        )

        return {

            "incident_id": incident_id,

            "severity": incident["severity"],

            "action": action

        }

    # -------------------------------------
    # Dispatch Workflow
    # -------------------------------------

    def dispatch_workflow(
        self,
        incident_id
    ):
        """
        Complete workflow:

        Assign volunteer
        Dispatch alert
        Escalate if required
        """

        assignment = self.assign_volunteer(
            incident_id
        )

        alert = self.dispatch_alert(
            incident_id
        )

        escalation = self.escalate_incident(
            incident_id
        )

        return {

            "assignment": assignment,

            "alert": alert,

            "escalation": escalation

        }

    # -------------------------------------
    # Alert History Entry
    # -------------------------------------

    def alert_log(
        self,
        incident_id
    ):

        if not self.incident_exists(
            incident_id
        ):
            return None

        incident = self.incidents[
            incident_id
        ]

        return {

            "incident": incident_id,

            "timestamp":
                self.current_time().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "severity":
                incident["severity"],

            "zone":
                incident["zone"],

            "volunteer":
                incident["assigned_volunteer"]

        }
    # -------------------------------------
    # Resolve Incident
    # -------------------------------------

    def resolve_incident(
        self,
        incident_id,
        resolution_notes="Resolved"
    ):
        """
        Resolve an active incident.
        """

        if not self.incident_exists(incident_id):

            return {

                "success": False,

                "message": "Incident not found."

            }

        incident = self.incidents[incident_id]

        incident["status"] = "Resolved"

        incident["resolved_at"] = self.current_time()

        incident["resolution_notes"] = resolution_notes

        # Calculate response duration

        response_duration = (

            incident["resolved_at"] -
            incident["reported_at"]

        ).total_seconds()

        incident["response_duration"] = round(
            response_duration,
            2
        )

        # Release assigned volunteer

        volunteer_id = incident.get(
            "assigned_volunteer"
        )

        if volunteer_id:

            self.release_volunteer(
                volunteer_id
            )

        # Move to history

        self.history.append(
            incident.copy()
        )

        del self.incidents[
            incident_id
        ]

        self.refresh_statistics()

        logging.info(
            "Incident %s resolved.",
            incident_id
        )

        return {

            "success": True,

            "incident": incident

        }

    # -------------------------------------
    # Close Multiple Incidents
    # -------------------------------------

    def resolve_all(self):
        """
        Resolve every active incident.
        """

        resolved = []

        for incident_id in list(
            self.incidents.keys()
        ):

            result = self.resolve_incident(
                incident_id
            )

            if result["success"]:

                resolved.append(
                    incident_id
                )

        return resolved

    # -------------------------------------
    # Incident History
    # -------------------------------------

    def incident_history(self):

        return self.history

    # -------------------------------------
    # History by Category
    # -------------------------------------

    def history_by_category(
        self,
        category
    ):

        return [

            incident

            for incident in self.history

            if incident["category"] == category

        ]

    # -------------------------------------
    # History by Severity
    # -------------------------------------

    def history_by_severity(
        self,
        severity
    ):

        return [

            incident

            for incident in self.history

            if incident["severity"] == severity

        ]

    # -------------------------------------
    # Incident Details
    # -------------------------------------

    def incident_details(
        self,
        incident_id
    ):
        """
        Search active and resolved incidents.
        """

        if incident_id in self.incidents:

            return self.incidents[
                incident_id
            ]

        for incident in self.history:

            if (
                incident["incident_id"]
                == incident_id
            ):

                return incident

        return None
    # -------------------------------------
    # Average Response Time
    # -------------------------------------

    def average_response_time(self):
        """
        Calculate average response duration
        of resolved incidents.
        """

        completed = [

            incident

            for incident in self.history

            if "response_duration" in incident

        ]

        if not completed:

            return 0

        total = sum(

            incident["response_duration"]

            for incident in completed

        )

        return round(

            total / len(completed),

            2

        )

    # -------------------------------------
    # Severity Analytics
    # -------------------------------------

    def severity_analytics(self):
        """
        Count resolved incidents
        by severity.
        """

        analytics = {

            severity: 0

            for severity in self.severity_levels

        }

        for incident in self.history:

            severity = incident["severity"]

            analytics[severity] = (

                analytics.get(severity, 0)

                + 1

            )

        return analytics

    # -------------------------------------
    # Category Analytics
    # -------------------------------------

    def category_analytics(self):
        """
        Count resolved incidents
        by category.
        """

        analytics = {

            category: 0

            for category in self.categories

        }

        for incident in self.history:

            category = incident["category"]

            analytics[category] = (

                analytics.get(category, 0)

                + 1

            )

        return analytics

    # -------------------------------------
    # Volunteer Utilization
    # -------------------------------------

    def volunteer_utilization(self):
        """
        Calculate how many incidents
        each volunteer handled.
        """

        utilization = {}

        for volunteer_id in self.volunteers:

            utilization[volunteer_id] = 0

        for incident in self.history:

            volunteer = incident.get(
                "assigned_volunteer"
            )

            if volunteer:

                utilization[volunteer] = (

                    utilization.get(volunteer, 0)

                    + 1

                )

        return utilization

    # -------------------------------------
    # Busiest Zone
    # -------------------------------------

    def busiest_zone(self):
        """
        Find the zone with the most incidents.
        """

        zones = {}

        for incident in self.history:

            zone = incident["zone"]

            zones[zone] = (

                zones.get(zone, 0)

                + 1

            )

        if not zones:

            return None

        return max(

            zones,

            key=zones.get

        )

    # -------------------------------------
    # Analytics Summary
    # -------------------------------------

    def analytics_summary(self):
        """
        Overall emergency analytics.
        """

        return {

            "average_response_time":
                self.average_response_time(),

            "severity":
                self.severity_analytics(),

            "categories":
                self.category_analytics(),

            "volunteers":
                self.volunteer_utilization(),

            "busiest_zone":
                self.busiest_zone()

        }
    # -------------------------------------
    # Dashboard Metrics
    # -------------------------------------

    def dashboard_metrics(self):
        """
        Generate dashboard metrics.
        """

        return {

            "active_incidents":
                self.active_incidents(),

            "resolved_incidents":
                self.resolved_incidents(),

            "registered_volunteers":
                len(self.volunteers),

            "available_volunteers":
                len(self.available_volunteers()),

            "busy_volunteers":
                len(self.volunteers) -
                len(self.available_volunteers()),

            "average_response_time":
                self.average_response_time(),

            "busiest_zone":
                self.busiest_zone()

        }

    # -------------------------------------
    # Resource Utilization
    # -------------------------------------

    def resource_utilization(self):
        """
        Estimate current utilization of
        emergency resources.
        """

        volunteers_total = self.resources.get(
            "volunteers",
            0
        )

        volunteers_busy = len(

            [

                volunteer

                for volunteer in self.volunteers.values()

                if volunteer["status"] == "Busy"

            ]

        )

        volunteer_percent = 0

        if volunteers_total > 0:

            volunteer_percent = round(

                (
                    volunteers_busy
                    /
                    volunteers_total
                ) * 100,

                2

            )

        return {

            "volunteers": {

                "total":
                    volunteers_total,

                "busy":
                    volunteers_busy,

                "utilization":
                    volunteer_percent

            },

            "ambulances":
                self.resources.get(
                    "ambulances",
                    0
                ),

            "medical_rooms":
                self.resources.get(
                    "medical_rooms",
                    0
                ),

            "security_staff":
                self.resources.get(
                    "security_staff",
                    0
                )

        }

    # -------------------------------------
    # Incident Trends
    # -------------------------------------

    def incident_trends(self):
        """
        Count incidents by date.
        """

        trends = {}

        for incident in self.history:

            date = incident[
                "reported_at"
            ].strftime(
                "%Y-%m-%d"
            )

            trends[date] = (

                trends.get(
                    date,
                    0
                ) + 1

            )

        return trends

    # -------------------------------------
    # Performance Report
    # -------------------------------------

    def performance_report(self):
        """
        Complete emergency performance report.
        """

        return {

            "dashboard":
                self.dashboard_metrics(),

            "analytics":
                self.analytics_summary(),

            "resources":
                self.resource_utilization(),

            "trends":
                self.incident_trends(),

            "generated_at":
                self.current_time().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

        }

    # -------------------------------------
    # Refresh Analytics
    # -------------------------------------

    def refresh_analytics(self):
        """
        Refresh analytics cache.
        """

        report = self.performance_report()

        self.statistics["last_updated"] = (
            self.current_time()
        )

        return report

    # -------------------------------------
    # Analytics Health
    # -------------------------------------

    def analytics_health(self):
        """
        Return analytics subsystem status.
        """

        return {

            "status": "Healthy",

            "history_records":
                len(self.history),

            "active_records":
                len(self.incidents),

            "last_updated":
                self.statistics.get(
                    "last_updated"
                )

        }
    # -------------------------------------
    # Export Active Incidents
    # -------------------------------------

    def export_active_incidents(self):
        """
        Export all active incidents.
        """

        return [

            incident.copy()

            for incident in self.incidents.values()

        ]

    # -------------------------------------
    # Export Resolved Incidents
    # -------------------------------------

    def export_resolved_incidents(self):
        """
        Export resolved incident history.
        """

        return [

            incident.copy()

            for incident in self.history

        ]

    # -------------------------------------
    # Search Incident History
    # -------------------------------------

    def search_history(
        self,
        keyword
    ):
        """
        Search resolved incidents by keyword.
        """

        keyword = keyword.lower()

        results = []

        for incident in self.history:

            fields = [

                incident["incident_id"],

                incident["category"],

                incident["severity"],

                incident["zone"],

                incident["description"]

            ]

            if any(

                keyword in str(field).lower()

                for field in fields

            ):

                results.append(incident)

        return results

    # -------------------------------------
    # Audit Log
    # -------------------------------------

    def audit_log(self):
        """
        Generate audit entries for
        active and resolved incidents.
        """

        logs = []

        # Active incidents

        for incident in self.incidents.values():

            logs.append({

                "incident_id":
                    incident["incident_id"],

                "status":
                    incident["status"],

                "timestamp":
                    incident["reported_at"],

                "zone":
                    incident["zone"],

                "severity":
                    incident["severity"]

            })

        # Resolved incidents

        for incident in self.history:

            logs.append({

                "incident_id":
                    incident["incident_id"],

                "status":
                    "Resolved",

                "timestamp":
                    incident.get(
                        "resolved_at",
                        incident["reported_at"]
                    ),

                "zone":
                    incident["zone"],

                "severity":
                    incident["severity"]

            })

        logs.sort(

            key=lambda item: item["timestamp"]

        )

        return logs

    # -------------------------------------
    # Export Analytics
    # -------------------------------------

    def export_analytics(self):
        """
        Export analytics information.
        """

        return {

            "dashboard":
                self.dashboard_metrics(),

            "analytics":
                self.analytics_summary(),

            "performance":
                self.performance_report(),

            "generated_at":
                self.current_time().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

        }

    # -------------------------------------
    # Export Resources
    # -------------------------------------

    def export_resources(self):
        """
        Export resource information.
        """

        return {

            "resources":
                self.available_resources(),

            "utilization":
                self.resource_utilization()

        }
    # -------------------------------------
    # Complete Emergency Report
    # -------------------------------------

    def complete_report(self):
        """
        Generate a complete emergency system report.
        """

        return {

            "generated_at":
                self.current_time().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "health":
                self.health(),

            "statistics":
                self.refresh_statistics(),

            "dashboard":
                self.dashboard_metrics(),

            "analytics":
                self.analytics_summary(),

            "resources":
                self.export_resources(),

            "active_incidents":
                self.export_active_incidents(),

            "resolved_incidents":
                self.export_resolved_incidents()

        }

    # -------------------------------------
    # JSON Export
    # -------------------------------------

    def export_json(self):
        """
        Return a JSON-serializable dictionary.
        """

        return {

            "system": "EmergencyAlertAI",

            "version": "1.0",

            "report": self.complete_report()

        }

    # -------------------------------------
    # Backup System State
    # -------------------------------------

    def backup_state(self):
        """
        Backup current in-memory state.
        """

        return {

            "incidents":
                self.export_active_incidents(),

            "history":
                self.export_resolved_incidents(),

            "volunteers":
                self.volunteers.copy(),

            "resources":
                self.resources.copy(),

            "statistics":
                self.statistics.copy()

        }

    # -------------------------------------
    # Restore System State
    # -------------------------------------

    def restore_state(self, backup):
        """
        Restore state from a backup dictionary.
        """

        self.incidents = {
            item["incident_id"]: item
            for item in backup.get("incidents", [])
        }

        self.history = backup.get("history", [])

        self.volunteers = backup.get(
            "volunteers",
            {}
        )

        self.resources = backup.get(
            "resources",
            {}
        )

        self.statistics = backup.get(
            "statistics",
            {}
        )

        self.refresh_statistics()

        logging.info(
            "EmergencyAlertAI state restored."
        )

        return True

    # -------------------------------------
    # Reset System
    # -------------------------------------

    def reset_system(self):
        """
        Clear all incidents and restore
        volunteer availability.
        """

        self.incidents.clear()
        self.history.clear()

        for volunteer in self.volunteers.values():
            volunteer["status"] = "Available"

        self.refresh_statistics()

        logging.warning(
            "EmergencyAlertAI system reset."
        )

        return True

    # -------------------------------------
    # System Information
    # -------------------------------------

    def system_info(self):
        """
        Return module metadata.
        """

        return {

            "module": "EmergencyAlertAI",

            "version": "1.0",

            "categories":
                list(self.categories.keys()),

            "zones":
                list(self.zones.keys()),

            "response_teams":
                self.response_teams,

            "resources":
                self.resources

        }
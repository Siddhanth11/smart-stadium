# services/qr_service.py

import os
import qrcode


class QRService:
    """
    Smart Stadium QR Code Service
    """

    def __init__(self):

        self.output_folder = "static/qrcodes"

        os.makedirs(
            self.output_folder,
            exist_ok=True
        )

    # ---------------------------------
    # Generate QR Code
    # ---------------------------------

    def generate_qr(
        self,
        ticket_id,
        data
    ):

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )

        qr.add_data(data)

        qr.make(fit=True)

        image = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        filename = f"{ticket_id}.png"

        filepath = os.path.join(
            self.output_folder,
            filename
        )

        image.save(filepath)

        return {

            "success": True,

            "ticket_id": ticket_id,

            "file": filepath

        }

    # ---------------------------------
    # Verify QR
    # ---------------------------------

    def verify_qr(
        self,
        ticket_id
    ):

        filename = os.path.join(

            self.output_folder,

            f"{ticket_id}.png"

        )

        if os.path.exists(filename):

            return {

                "valid": True,

                "message":
                    "QR Code Found"

            }

        return {

            "valid": False,

            "message":
                "QR Code Not Found"

        }

    # ---------------------------------
    # Delete QR
    # ---------------------------------

    def delete_qr(
        self,
        ticket_id
    ):

        filename = os.path.join(

            self.output_folder,

            f"{ticket_id}.png"

        )

        if os.path.exists(filename):

            os.remove(filename)

            return {

                "success": True,

                "message":
                    "QR Code Deleted"

            }

        return {

            "success": False,

            "message":
                "QR Code Not Found"

        }

    # ---------------------------------
    # List QR Codes
    # ---------------------------------

    def list_qr_codes(self):

        return os.listdir(
            self.output_folder
        )

    # ---------------------------------
    # Health Check
    # ---------------------------------

    def health(self):

        return {

            "service": "QR Service",

            "status": "Running",

            "total_qr_codes":
                len(self.list_qr_codes())

        }


# Singleton Object

qr_service = QRService()
from django import forms
from django.core.exceptions import ValidationError
from .models import Booking, BookingStatus


class BookingForm(forms.ModelForm):
    """Form for creating and updating booking reservations."""

    class Meta:
        model = Booking
        fields = ("check_in", "check_out", "comment")
        widgets = {
            "check_in": forms.DateInput(attrs={"type": "date", "required": True}),
            "check_out": forms.DateInput(attrs={"type": "date", "required": True}),
            "comment": forms.Textarea(attrs={"rows": 3, "placeholder": "Add any special requests..."}),
        }
        labels = {
            "check_in": "Check-in Date",
            "check_out": "Check-out Date",
            "comment": "Special Requests",
        }

    def clean(self):
        """Validate that check-out date is after check-in date."""
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

        if check_in and check_out and check_out <= check_in:
            raise ValidationError("Check-out date must be after check-in date.")

        return cleaned_data

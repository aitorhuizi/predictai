from rest_framework import serializers

class TuSerializer(serializers.Serializer):

    TARGET_COL_CHOICES = (
        ('falloIzquierdo', 'Fallo Izquierdo'),
        ('falloDerecho', 'Fallo Derecho'),
    )

    target_col = serializers.ChoiceField(choices=TARGET_COL_CHOICES)

    '''def validate_field(self, value):

        if value not in ['falloIzquierdo', 'falloDerecho']:
            raise serializers.ValidationError("Invalid target column name")

        return value'''